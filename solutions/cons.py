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
    >>> cons(collection)
    ('ATGCAACT', ([5, 1, 0, 0, 5, 5, 0, 0], [0, 0, 1, 4, 2, 0, 6, 1], [1, 1, 6, 3, 0, 1, 0, 0], [1, 5, 0, 0, 0, 1, 1, 6]))
    '''
    profile = profile_matrix(collection)
    consensus = consensus_string(profile)
    return consensus, profile

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
