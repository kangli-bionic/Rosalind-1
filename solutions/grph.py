from collections import defaultdict

def grph(fastas, sub):
    ''' Rosalind Problem 11
    Overlap Graphs
    
    Given: A collection of DNA strings in FASTA format having
    total length at most 10 kbp.

    Return: The adjacency list corresponding to O sub 3. 
    You may return edges in any order.

    >>> from rutility.parsers import fasta 
    >>> fastas = fasta(iter('>Rosalind_0498 AAATAAA '
    ...                     '>Rosalind_2391 AAATTTT '
    ...                     '>Rosalind_2323 TTTTCCC '
    ...                     '>Rosalind_0442 AAATCCC '
    ...                     '>Rosalind_5013 GGGTGGG '.split()))
    >>> for g in grph(fastas, 3):
    ...     print g
    ('Rosalind_0498', 'Rosalind_2391')
    ('Rosalind_0498', 'Rosalind_0442')
    ('Rosalind_2391', 'Rosalind_2323')
    '''

    heads_dict, tails_dict = defaultdict(list), defaultdict(list)
    
    for f in fastas:
        heads_dict[f.data[:sub]].append(f.name)
        tails_dict[f.data[-sub:]].append(f.name)

    results = []
    for tails in tails_dict:
        for tail in tails_dict[tails]:
            results.append((tail, heads_dict[tails]))

    for head, tails in results:
        for tail in tails:
            if tail != head:
                yield head, tail

