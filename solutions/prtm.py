from rutility.maps import monoisotopic_amino


def prtm(protein):
    ''' Calculating Protein Mass

    Given: A protein string P of length at most 1000 aa.

    Return: The weight of P.
    Consult the monoisotopic mass table.

    >>> round(prtm('SKADYEK'), 3)
    821.392
    '''
    return sum([monoisotopic_amino[a] for a in protein])
