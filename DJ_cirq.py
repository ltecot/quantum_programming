import random
import cirq
from cirq import H, X, CNOT, measure
import argparse
import time

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("-n",dest="n", type=int, required=True)
    #parser.add_argument("-f",dest="f", type=create_lambda_with_globals, required=True)
    args = parser.parse_args()

    n = args.n
    #f = args.f  # test_f_4, test_f_5
    trials = 10

    start = time.time()

    # Choose qubits to use.
    input_qubits = [cirq.GridQubit(i, 0) for i in range(n)]
    output_qubit = cirq.GridQubit(n, 0)

    # Pick coefficients for the oracle and create a circuit to query it.
    secret_function = random.randint(0, 1)
    oracle = make_oracle(input_qubits, output_qubit, secret_function)
    print('Secret function: ',end='')
    if secret_function == 0: 
        print('Constant')
    else: 
        print('Balanced')

    # Embed the oracle into a quantum circuit querying it exactly once.
    circuit = make_deutsch_jozsa_circuit(input_qubits, output_qubit, oracle)
    print('Circuit:')
    print(circuit)
    
    # Simulate the circuit.
    simulator = cirq.Simulator()
    result = simulator.run(circuit)
    print(result)


    '''
    # Sample from the circuit a couple times.
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=trials)
    frequencies = result.histogram(key='result', fold_func=bitstring)
    print('Sampled results:\n{}'.format(frequencies))

    # Check if we actually found the secret value.
    most_common_bitstring = frequencies.most_common(1)[0][0]
    print('Most common matches secret factors:\n{}'.format(
        most_common_bitstring == bitstring(secret_function)))
    '''


    end = time.time()
    print("Execution time: ", end - start)

def create_lambda_with_globals(s):
    return eval(s, globals())

def make_oracle(input_qubits, output_qubit, secret_function):
    """Gates implementing the function f(a) = a·factors + bias (mod 2)."""

    if secret_function==0:
        yield cirq.X(output_qubit)

    if secret_function==1:
        yield cirq.CNOT(input_qubits[0], output_qubit)


def make_deutsch_jozsa_circuit(input_qubits, output_qubit, oracle):
    """Solves for factors in f(a) = a·factors + bias (mod 2) with one query."""

    c = cirq.Circuit()

    # Initialize qubits.
    c.append([
        cirq.X(output_qubit),
        cirq.H(output_qubit),
        cirq.H.on_each(*input_qubits),
    ],strategy=cirq.InsertStrategy.NEW_THEN_INLINE)

    # Query oracle.
    c.append(oracle)

    # Measure in X basis.
    c.append([
        cirq.H.on_each(*input_qubits),
        cirq.measure(*input_qubits, key='result')
    ],strategy=cirq.InsertStrategy.NEW_THEN_INLINE)

    return c


def bitstring(bits):
    return ''.join(str(int(b)) for b in bits)


if __name__ == '__main__':
    main()