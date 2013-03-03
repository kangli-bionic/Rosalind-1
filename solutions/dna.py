def dna(dnastring):
    ''' Counting DNA Nucleotides

    Given: A DNA string s of length at most 1000 nt.

    Return: Four integers (separated by spaces) counting the
    respective number of times that the symbols 'A', 'C', 'G',
    and 'T' occur in s.
    >>> testdna = ('AGCTTTTCATTCTGACTGCAACGGGCAATATGTC'
    ...            'TCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')
    >>> dna(testdna)
    [20, 12, 17, 21]
    '''
    return [dnastring.count(nt) for nt in ("A C G T").split()]
