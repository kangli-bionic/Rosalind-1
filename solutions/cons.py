from rutility.genetics import profile_matrix, consensus_string


def cons(collection):
    ''' Consensus and Profile

    Given: A collection of at most 10 DNA strings of equal length
    (at most 1 kbp) in FASTA format.

    Return: A consensus string and profile matrix for the
    collection. (If several possible consensus strings exist,
    then you may return any one of them.)

    >>> collection = ['ATCCAGCT', 'GGGCAACT', 'ATGGATCT',
    ...               'AAGCAACC', 'TTGGAACT', 'ATGCCATT',
    ...               'ATGGCACT']
    >>> con = cons(collection)
    >>> print con[0]
    ATGCAACT
    >>> for s in con[1]:
    ...     print s
    [5, 1, 0, 0, 5, 5, 0, 0]
    [0, 0, 1, 4, 2, 0, 6, 1]
    [1, 1, 6, 3, 0, 1, 0, 0]
    [1, 5, 0, 0, 0, 1, 1, 6]
    '''
    profile = profile_matrix(collection)
    consensus = consensus_string(profile)
    return consensus, profile
