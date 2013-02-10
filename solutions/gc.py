from rutility.parsers import fasta, Fasta

def gc(fasta):
    ''' Rosalind Problem 4
    Identifying Unknown DNA Quickly.

    Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

    Return: The ID of the string having the highest GC-content, followed by the 
    GC-content of that string. Rosalind allows for a default error of 0.001 in all 
    decimal answers unless otherwise stated; please see the note on absolute error 
    below.
        
    >>> data = Fasta(name='Rosalind_6404', data='CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG')
    >>> gc(data)
    53.75
    '''
    data = fasta.data
    return (data.count('G') + data.count('C')) / float(len(data)) * 100