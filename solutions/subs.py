def subs(dna, sub):
    ''' Finding a Motif in DNA

    Given: Two DNA strings s and t (each of length at most 1 kbp).

    Return: All locations of t as a substring of s

    >>> dna = 'GATATATGCATATACTT'
    >>> sub = 'ATAT'
    >>> subs(dna, sub)
    [2, 4, 10]
    '''
    results = []
    for i in xrange(len(dna)-len(sub)+1):  # +1 adjust for end of string
        if sub == dna[i:i+len(sub)]:
            results.append(i+1)  # +1 adjust for 0 index
    return results