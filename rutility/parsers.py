from collections import namedtuple
from fileops import readfile
from itertools import izip_longest

Fasta = namedtuple("Fasta", "name, data")

def fasta(iterator):
    results = [iterator.next().strip()]
    try:
        while True:
            item = iterator.next().strip()
            while item[0] != '>':
                results.append(item)
                item = iterator.next().strip()
            yield Fasta(results[0][1:], ''.join(results[1:]))
            results = [item]
    except:
        yield Fasta(results[0][1:], ''.join(results[1:]))
    
def fastatest(fn):
    ''' Test function for the fasta parser. 
    >>> fastatest(fasta)
    Fastatest pass!
    '''
    # static data
    testdata = iter([i for i in """>Rosalind_6404
    CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
    TCCCACTAATAATTCTGAGG
    >Rosalind_5959
    CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
    ATATCCATTTGTCAGCAGACACGC
    >Rosalind_0808
    CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
    TGGGAACCTGCGGGCAGTAGGTGGAAT""".split('\n')])

    # data from a file
    f = readfile('fastatest.txt')
    with f:
        tests = (fn(testdata), fn(f))
        for t in tests:
            a, b, c = t.next(), t.next(), t.next()
            assert a.name=='Rosalind_6404' and a.data=='CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG'
            assert b.name=='Rosalind_5959' and b.data=='CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC'
            assert c.name=='Rosalind_0808' and c.data=='CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT'

        print "Fastatest pass!"

def triplets(nts):
    ''' Continusly yields triplets from a string of nucleotides. '''
    nts_iter = iter(nts)
    while True:
        yield ''.join((nts_iter.next(), nts_iter.next(), nts_iter.next()))
         
def grouper(iterable, n):
    "Collect data into fixed-length chunks or blocks"
    args = [iter(iterable)] * n
    pick = izip_longest(fillvalue=None, *args)
    while True:
        yield [i for i in pick.next() if i]