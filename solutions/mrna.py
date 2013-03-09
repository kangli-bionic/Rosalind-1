from collections import defaultdict
from rutility.maps import rna_codons


def mrna(prot):
    ''' Inferring mRNA from Protein
    
    Given: A protein string of length at most 1000 aa.

    Return: The total number of different RNA strings
    from which the protein could have been translated,
    modulo 1,000,000. (Don't neglect the importance of
    the stop codon in protein translation.)
    
    >>> mrna(prot)
    12
    '''
    reverse = defaultdict(list)
    for k, v in rna_codons.items():
        reverse[v].append(k)

    return reduce(lambda x, y: x*y,
                  [len(reverse[p]) for p in prot] +
                  [len(reverse['Stop'])])
