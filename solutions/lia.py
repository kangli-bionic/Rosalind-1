from scipy.misc import comb


def lia(k, n):
    ''' Mendel's Second Law

    Given: Two positive integers k (k<=7) and N (N<=2k). In this problem,
    we begin with Tom, who in the 0th generation has genotype Aa Bb.
    Tom has two children in the 1st generation,
    each of whom has two children, and so on.

    Each organism always mates with an organism having genotype Aa Bb.

    Return: The probability that at least N Aa Bb organisms will belong to the
    k-th generation of Tom's family tree (don't count the Aa Bb mates at each
    level). Assume that Mendel's second law holds for the factors.

    >>> round(lia(2, 1), 3)
    0.684
    '''
    t = 2**k
    return sum([comb(t, i, 1) * 0.25**i * 0.75**(t-i) for i in range(n, t+1)])
