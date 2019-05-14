# Utilities, mostly for U_f creation
# Reference repos:
# https://github.com/msohaibalam/quantum_algorithms_from_scratch/blob/master/Bernstein-Vazirani%20Algorithm.ipynb
# https://github.com/msohaibalam/quantum_algorithms_from_scratch/blob/master/Deutsch's%20Algorithm.ipynb

import numpy as np
import itertools
from bernstein_vazirani_classical import test_f_1, test_f_2, test_f_3
from deutsch_jozsa_classical import balanced_f, constant_f, pseudo_balanced_f

# Convert results from measurment into full state per trial
def process_results(result, n, t):
    trials = []
    for ti in range(t):
        trial = ''
        for ni in range(n):
            trial = str(result[ni][ti]) + trial
        trials.append(trial[:-1])
    return trials

# Converts string-representation of qubit into a vector.
def ket(qs):
    val_map = {'0': np.array([[1], [0]]), 
               '1': np.array([[0], [1]])}
    k = val_map[qs[0]]  # Ket
    for i in range(1, len(qs)):
        k = np.kron(k, val_map[qs[i]])
    return k

# Calculates the outer product of the state input.
def outer_product(qs):
    k = ket(qs)  # Ket
    b = np.transpose(k)  # Bra
    proj = np.kron(k, b)
    return proj

# Returns all calls of f(x) for all possible inputs.
# Stores result in a dict.
def f_x(f, n):
    qs = []
    for q in itertools.product(['0', '1'], repeat=n):
        qs.append(''.join(q))
    fx = {}
    for q in qs:
        fx[q] = f(q)
    return fx

# p.defgate("U_f", create_Uf_matrix())
# p.inst(("U_f",) + tuple(range(n+1)[::-1]))
# Takes in a lambda function and the input size, n.
def create_Uf_matrix(f, n):
    N = 2**(n+1)
    mat = np.zeros(shape=(N, N))
    fx = f_x(f, n)
    for k, v in fx.items():
        mat += np.kron(outer_product(k), np.eye(2) + v * (np.array([[-1, 1], [1, -1]])))
    return mat

def test_uf_matrix():
    print(create_Uf_matrix(balanced_f, 3))
    print(create_Uf_matrix(constant_f, 3))
    print(create_Uf_matrix(pseudo_balanced_f, 3))
    print(create_Uf_matrix(test_f_1, 5))
    # print(create_Uf_matrix(test_f_2, 20))
    print(create_Uf_matrix(test_f_3, 2))

if __name__ == "__main__":
    test_uf_matrix()