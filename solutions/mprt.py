import re
from rutility.parsers import protein_motif, uniprot


def mprt(prot, shorthand):
    ''' Motif Implies Function

    Given: At most 15 UniProt Protein Database access IDs.

    Return: For each protein possessing the N-glycosylation motif,
    output its given access ID followed by a list of locations in
    the protein string where the motif can be found.

    >>> prot = uniprot('B5ZC00')
    >>> mprt(prot.data, 'N{P}[ST]{P}')
    [85, 118, 142, 306, 395]

    >>> mprt('NMSP', 'N{P}[ST]{P}')
    []
    '''
    n, motif = protein_motif(shorthand)
    matches = re.finditer(motif, prot)
    return [m.end() - n + 1 for m in matches]

