from rutility.maps import rna_codons
from solutions.rna import rna
from solutions.prot import prot
from solutions.revc import revc


def orf(dna):
    ''' Open reading Frames

    Given: A DNA string s of length at most 1 kbp in FASTA format.

    Return: Every distinct candidate protein string that can be
    translated from ORFs of s. Strings can be returned in any order.
    >>> dna = ('AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAG'
    ...        'AGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG')
    >>> results = orf(dna)
    >>> for r in sorted(results):
    ...     print r
    M
    MGMTPRLGLESLLE
    MLLGSFRLIPKETLIQVAGSSPCNLS
    MTPRLGLESLLE
    '''
    rnadna = [rna(dna), rna(revc(dna))]

    frames, results = [], []
    for r in rnadna:
        frames.append(r)
        frames.append(r[1:])
        frames.append(r[2:])

    for frame in frames:
        protein = prot(frame, stop=False)
        for i in xrange(len(protein)):
            if protein[i] == 'M':
                e = protein[i:].find('$')
                results.append(protein[i:i+e])

    return [i for i in list(set(results)) if i != '']
