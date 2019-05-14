import numpy as np
from pyquil import get_qc, Program
from pyquil.api import QuantumComputer
from pyquil.gates import *

from deutsch_jozsa_classical import constant_f, balanced_f
from util import create_Uf_matrix, process_results

import time
import sys

if len(sys.argv) < 2:
    print('Usage: python3 DJ_pyquil.py <n>')
    exit()

n = int(sys.argv[1]) # TODO: main function input
t = 5
f = constant_f
# f = balanced_f

start = time.time()

p = Program()
p.defgate("U_f", create_Uf_matrix(f, n))

p.inst(X(0))
p.inst(H(0))
for q in range(1, n+1):
    p.inst(H(q))
p.inst(("U_f",) + tuple(range(n+1)[::-1]))  # Applying U_f
for q in range(1, n+1):
    p.inst(H(q))

# You can make any 'nq-qvm' this way for any reasonable 'n'
qc = get_qc(str(n+1)+'q-qvm')
result = qc.run_and_measure(p, trials = t)

end = time.time()

print(process_results(result, n+1, t))
print("Execution time: ", end - start)