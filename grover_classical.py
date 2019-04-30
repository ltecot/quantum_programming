# Classical Implementation of Grover's Problem.
# We'll just use strings to represent bit-strings of 0 and 1.

import random

# Return 0 if there exists a bit string of length "n" where f(x) = 1, 0 otherwise.
# f takes in a string of 0s and 1s and returns an int of 0 or 1.
#
# We can just iterate over all inputs and return 1 if one returns 1.
# If none are found return 0.
def grover(f, n):
	b_format = "{0:0" + str(n) + "b}"
	i = 0
	while i < 2**(n):
		if f(b_format.format(i)) == 1:
			return 1
		i += 1
	return 0

# TESTING

def test_0(x):
	return 0

def test_1(x):
	return 1

def test_only_one(x):
	if '0' not in x:
		return 1
	return 0

def test_random(x):
	return random.randint(0, 1)

def test_gp():
	assert grover(test_only_one, 5) == 1
	assert grover(test_0, 10) == 0
	assert grover(test_1, 15) == 1
	assert grover(test_random, 20) == 1

if __name__ == '__main__':
	test_gp()