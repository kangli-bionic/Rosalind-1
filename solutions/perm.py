from itertools import permutations
from math import factorial

def perm(n):
    return factorial(n), permutations(xrange(1, n+1))