import numpy as np
from pyquil import Program
from pyquil.api import QuantumComputer
from pyquil.gates import *


dj = Program()

N = 5 
A = np.random.choice([0, 1], size=(N))
B = random.randint(0,1)

print(A)
print(B)

dj.inst(X(0))
dj.inst(H(0))

for qubit in range(1, N+1):
    dj.inst(H(qubit))


dj.inst(("U_f",)

for qubit in range(1, N+1):
    dj.inst(H(qubit))


qc = get_qc('1q-qvm')  # You can make any 'nq-qvm' this way for any reasonable 'n'
executable = qc.compile(dj)
result = qc.run_and_measure(executable, trails = 50)
print(result)


