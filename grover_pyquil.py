# Quantum Grover's algorithm. Implemented as described in lecture.

import numpy as np
from pyquil import get_qc, Program
from pyquil.api import QuantumComputer
from pyquil.gates import *

from grover_classical import test_only_one, test_01, test_000, test_10010, test_1111
from util import create_Z0_matrix, create_Zf_matrix, process_results

import time
import sys
import argparse
import math

def create_lambda_with_globals(s):
    return eval(s, globals())

parser = argparse.ArgumentParser()

parser.add_argument("-n",dest="n", type=int, required=True)
parser.add_argument("-f",dest="f", type=create_lambda_with_globals, required=True)
args = parser.parse_args()

n = args.n
f = args.f

start = time.time()

p = Program()
p.defgate("Z_0", create_Z0_matrix(n))
p.defgate("Z_f", create_Zf_matrix(f, n))
# p.defgate("neg_I", -np.identity(2**n))

num_iter = math.floor((math.pi / 4) * math.sqrt(2**n))

# Initial Hadamard
for q in range(n):
    p.inst(H(q))

# Repeat G
for i in range(num_iter):
    p.inst(("Z_f",) + tuple(range(n)[::-1]))
    for q in range(n):
        p.inst(H(q))
    p.inst(("Z_0",) + tuple(range(n)[::-1]))
    for q in range(n):
        p.inst(H(q))
    # p.inst(("neg_I",) + tuple(range(n)[::-1]))

# You can make any 'nq-qvm' this way for any reasonable 'n'
qc = get_qc(str(n+1)+'q-qvm')
qc.compiler.client.timeout = 100
result = qc.run_and_measure(p, trials = 1)

end = time.time()

print(process_results(result, n, 1))
print("Execution time: ", end - start)