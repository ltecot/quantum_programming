import itertools
import numpy as np
from pyquil import get_qc, Program
from pyquil.gates import *

from simon_classical import test_wiki , test_wiki_2, test_linear
from util import *

import time
import sys
import argparse

def create_lambda_with_globals(s):
    return eval(s, globals())

parser = argparse.ArgumentParser()

parser.add_argument("-n",dest="n", type=int, required=True)
parser.add_argument("-f",dest="f", type=create_lambda_with_globals, required=True)
args = parser.parse_args()

n = args.n
f = args.f # test_wiki

M = []

start = time.time()

while rank(M) < n - 1:
    p = Program()

    p.defgate("B_f", create_Bf_matrix(f, n))

    for q in range(n):
        p.inst(I(q))
    for q in range(n, n * 2):
        p.inst(H(q))

    p.inst(("B_f",) + tuple(range(n*2)[::-1]))

    for q in range(n, n * 2):
        p.inst(H(q))

    qc = get_qc(str(n*2)+'q-qvm')
    qc.compiler.client.timeout = 100
    result = qc.run_and_measure(p, trials = 1)
    y = list(process_results(result, n*2, 1)[0][:n])
    y = [int(i) for i in y]
    y.append(0)

    M = new_sample(M, y)

    del p

end  = time.time()

print ("s: ", solve_reduced_row_echelon_form(M))
print("Execution time: ", end - start)