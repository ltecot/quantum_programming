import numpy as np
from pyquil import Program
from pyquil.api import QuantumComputer
from pyquil.gates import *


bv = Program()

N = 5 
A = np.random.choice([0, 1], size=(N))
B = random.randint(0,1)

print(A)
print(B)


