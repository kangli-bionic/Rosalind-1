from rutility.utility import common_substrings

def lcsm(collection):
    ''' Rosalind Problem 14
    Given: A collection of k (k<100) DNA strings of length 
    at most 1 kbp each in FASTA format.

    Return: A longest common substring of the collection. 
    (If multiple solutions exist, you may return any 
    single solution.)
    
    >>> from rutility.parsers import fasta
    >>> collection = ['GATTACAGATTACAGATTACA', 'GATTACATAGACCA', 'GATTACAATACA']
    >>> lcsm(collection)
    'GATTACA'
    '''
    _collection = iter(collection)
    common = ' '.join(list(common_substrings(_collection.next(), _collection.next(), 6)))

    while True:
        try:
            common = ' '.join(list(common_substrings(common, _collection.next(), 6)))
        except StopIteration:
            return common