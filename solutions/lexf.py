from itertools import product, repeat


def lexf(lex, perm):
    ''' Enumerating k-mers Lexicographically

    Given: A collection of at most 10 symbols defining an
    ordered alphabet, and a positive integer n (n?10).

    Return: All strings of length n that can be formed from
    the alphabet, ordered lexicographically.

    >>> lex = 'TAGC'
    >>> p = lexf(lex, 2)
    >>> for i in p:
    ...     print i
    TT
    TA
    TG
    TC
    AT
    AA
    AG
    AC
    GT
    GA
    GG
    GC
    CT
    CA
    CG
    CC
    '''
    for p in list(product(*repeat(lex, perm))):
        yield ''.join(p)
