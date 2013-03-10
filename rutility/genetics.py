from itertools import product
from itertools import chain

from maps import dihybrid


def profile_matrix(collection):
    rotate = ["".join(i) for i in zip(*collection)]
    a, c, g, t = [[] for i in range(4)]

    for row in rotate:
        a.append(row.count('A'))
        c.append(row.count('C'))
        g.append(row.count('G'))
        t.append(row.count('T'))
    return a, c, g, t


def consensus_string(profile):
    return ''.join(['ACGT'[j] for j in [row.index(max(row))
                    for row in [i for i in zip(*profile)]]])


def dihybrid_cross(m, f):
    ''' Given a pair of dihybrids, returns a list of 16 offspring.
    >>> hybrids = dihybrid_cross('AAbb', 'aaBB')
    >>> sum([hybrid == 'AaBb' for hybrid in hybrids])
    16
    >>> hybrids = dihybrid_cross('AaBb', 'AaBb')
    >>> len(set(hybrids))
    16
    >>> hybrids = dihybrid_cross('a', 'a')
    >>> sum([hybrid == 'AABB' for hybrid in hybrids])
    16
    '''
    if len(m) == 1:
        m = dihybrid[m]
    if len(f) == 1:
        f = dihybrid[f]

    mating = product(product(m[:2], m[2:]), product(f[:2], f[2:]))
    return [''.join([a, c, d, b]) for
            a, b, c, d in [list(chain(x, y)) for
                           x, y in mating]]
