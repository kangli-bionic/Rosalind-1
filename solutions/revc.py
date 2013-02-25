from string import translate, maketrans
def revc(dnastring):
    ''' The Secondary and Tertiary Structures of DNA

    Given: A DNA string s of length at most 1000 bp.

    Return: The reverse complement sc of s. 
        
    >>> revc("AAAACCCGGT")
    'ACCGGGTTTT'
    '''

    translation = maketrans("ATCG", "TAGC")
    return translate(dnastring, translation)[::-1]