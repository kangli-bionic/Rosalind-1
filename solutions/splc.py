from solutions.prot import prot
from solutions.rna import rna


def splc(dna, introns):
    ''' RNA Splicing

    Given: A DNA string s (of length at most 1 kbp) and a
    collection of substrings of s acting as introns. All
    strings are given in FASTA format.

    Return: A protein string resulting from transcribing and
    translating the exons of s. (Note: Only one solution will
    exist for the dataset provided.)

    >>> dna = ('ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATC'
    ...        'TCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGT'
    ...        'TTGCGCCTAG')
    >>> introns = ['ATCGGTCGAA', 'ATCGGTCGAGCGTGT']
    >>> splc(dna, introns)
    'MVYIADKQHVASREAYGHMFKVCA'
    '''
    for intron in sorted(introns, key=len, reverse=True):
        dna = ''.join(dna.split(intron))
    return prot(rna(dna))
