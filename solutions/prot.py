from rutility.maps import rna_codons
from rutility.parsers import triplets


def prot(rna):
    ''' Protein Translation

    Given: An RNA string s corresponding to a strand of mRNA
    (of length at most 10 kbp).

    Return: The protein string encoded by s.

    >>> rna = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
    >>> prot(rna)
    'MAMAPRTEINSTRING'
    '''
    result = []
    for triplet in triplets(rna):
        amino = rna_codons[triplet]
        if amino == 'Stop':
            return "".join(result)
        else:
            result.append(amino)
    return "".join(result)
