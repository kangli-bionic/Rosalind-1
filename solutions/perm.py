from itertools import permutations
from math import factorial


def perm(n):
    ''' Enumerating Gene Orders

    Given: A positive integer n >= 7.

    Return: The total number of permutations of length n,
    followed by a list of all such permutations (in any order).
    >>> p = perm(3)
    >>> p[0]
    6
    >>> sorted(list(p[1]))
    [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
    '''
    return factorial(n), permutations(xrange(1, n+1))
