from itertools import product
from itertools import combinations_with_replacement
from itertools import chain


def reversemap(map):
    ''' Reverses the k:v mapping of a dictionary.
    Throws out repeated elements. '''
    return {v: k for v, k in zip(map.values(), map.keys())}

rna_codons = {'GUC': 'V', 'ACC': 'T', 'GUA': 'V', 'GUG': 'V',
              'GUU': 'V', 'AAC': 'N', 'CCU': 'P', 'UGG': 'W',
              'AGC': 'S', 'AUC': 'I', 'CAU': 'H', 'AAU': 'N',
              'AGU': 'S', 'ACU': 'T', 'CAC': 'H', 'ACG': 'T',
              'CCG': 'P', 'CCA': 'P', 'ACA': 'T', 'CCC': 'P',
              'UGU': 'C', 'GGU': 'G', 'UCU': 'S', 'GCG': 'A',
              'UGC': 'C', 'CAG': 'Q', 'GAU': 'D', 'UAU': 'Y',
              'CGG': 'R', 'UCG': 'S', 'AGG': 'R', 'GGG': 'G',
              'UCC': 'S', 'UCA': 'S', 'UAA': '$', 'GGA': 'G',
              'UAC': 'Y', 'GAC': 'D', 'GAA': 'E', 'AUA': 'I',
              'GCA': 'A', 'CUU': 'L', 'GGC': 'G', 'AUG': 'M',
              'UGA': '$', 'CUG': 'L', 'GAG': 'E', 'CUC': 'L',
              'AGA': 'R', 'CUA': 'L', 'GCC': 'A', 'AAA': 'K',
              'AAG': 'K', 'CAA': 'Q', 'UUU': 'F', 'CGU': 'R',
              'CGA': 'R', 'GCU': 'A', 'UAG': '$', 'AUU': 'I',
              'UUG': 'L', 'UUA': 'L', 'CGC': 'R', 'UUC': 'F'}

hybrid_mating = {'h': 'dhhr', 'r': 'hhrr', 'd': 'ddhh'}

hybrid = {k: ''.join(v) for k, v in
          zip('dhr', combinations_with_replacement('Aa', 2))}

dihybrid = {k: ''.join(v) for k, v in
            zip('abcdefghijklmnop',
                [list(chain(x, y)) for x, y in
                 product(product('Aa', 'Aa'), product('Bb', 'Bb'))])}

monoisotopic_amino = {'A': 71.03711, 'C': 103.00919, 'E': 129.04259,
                      'D': 115.02694, 'G': 57.02146, 'F': 147.06841,
                      'I': 113.08406, 'H': 137.05891, 'K': 128.09496,
                      'M': 131.04049, 'L': 113.08406, 'N': 114.04293,
                      'Q': 128.05858, 'P': 97.05276, 'S': 87.03203,
                      'R': 156.10111, 'T': 101.04768, 'W': 186.07931,
                      'V': 99.06841, 'Y': 163.06333}
