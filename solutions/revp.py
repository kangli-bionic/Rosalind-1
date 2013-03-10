from solutions.revc import revc


def revp(dna):
    ''' Locating Restriction Sites

    Given: A DNA string of length at most 1 kbp in FASTA format.

    Return: The position and length of every reverse palindrome
    in the string having length between 4 and 12. You may return
    these pairs in any order.

    >>> dna = 'TCAATGCATGCGGGTCTATATGCAT'
    >>> results = revp(dna)
    >>> for r in sorted(list(results)):
    ...     print r
    (4, 6)
    (5, 4)
    (6, 6)
    (7, 4)
    (17, 4)
    (18, 4)
    (20, 6)
    (21, 4)
    '''
    for i in xrange(4, 12+1):
        for j in xrange(len(dna)-i+1):
            if dna[j:j+i] == revc(dna[j:j+i]):
                yield j+1, i
