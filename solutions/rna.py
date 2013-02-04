from string import translate, maketrans
def rna(rnastring):
    ''' Rosalind Problem 2
        The Second Nucleic Acid.

        Given: A DNA string t having length at most 1000 nt.

        Return: The transcribed RNA string of t.
        
        >>> rna("GATGGAACTTGACTACGTAAATT")
        'GAUGGAACUUGACUACGUAAAUU'
        '''

    translation = maketrans('T', 'U')
    return translate(rnastring, translation)
