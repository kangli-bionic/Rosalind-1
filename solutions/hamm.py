def hamm(s, t):
    ''' Counting Point Mutations

    Given: Two DNA strings s and t of equal length
    (not exceeding 1 kbp).

    Return: The Hamming distance dH(s,t).

    >>> s = "GAGCCTACTAACGGGAT"
    >>> t = "CATCGTAATGACGGCCT"
    >>> hamm(s, t)
    7
    '''
    return sum([1 for x, y in zip(s, t) if x != y])
