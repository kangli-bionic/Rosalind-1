from collections import namedtuple
from fileops import readfile
from itertools import izip_longest
import requests
import re
from maps import rna_codons

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

    # static results
    adata = ('CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCT'
             'CTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG')
    bdata = ('CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCC'
             'AGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC')
    cdata = ('CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAA'
             'CGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT')

    # data from a file
    f = readfile('fastatest.txt')
    with f:
        tests = (fn(testdata), fn(f))
        for t in tests:
            a, b, c = t.next(), t.next(), t.next()
            assert a.name == 'Rosalind_6404' and a.data == adata
            assert b.name == 'Rosalind_5959' and b.data == bdata
            assert c.name == 'Rosalind_0808' and c.data == cdata

        print "Fastatest pass!"


def triplets(nts):
    ''' Continusly yields triplets from a string of nucleotides. '''
    nts_iter = iter(nts)
    while True:
        yield ''.join((nts_iter.next(), nts_iter.next(), nts_iter.next()))


def grouper(iterable, n):
    ''' Collect data into fixed-length chunks or blocks. '''
    args = [iter(iterable)] * n
    pick = izip_longest(fillvalue=None, *args)
    while True:
        yield [i for i in pick.next() if i]


def uniprot(protname):
    ''' Given a UniProt access ID, returns that ID's fasta object.'''
    website = r'http://www.uniprot.org/uniprot/{}.fasta'.format(protname)
    r = requests.get(website)
    return fasta(iter(r.text.split('\n'))).next()


def _protein_motif(shorthand):
    ''' Returns a list of sets to iteratively match objects with. '''
    sh = iter(shorthand)

    codons = set(rna_codons.values())
    codons.remove('Stop')
    include, exclude = set('[]'), set('{}')

    temp = []
    while True:
        s = sh.next()
        if s not in include | exclude:
            yield set(s)

        if s in include:
            s = sh.next()
            while s not in include:
                temp.append(s)
                s = sh.next()
            yield set(temp)
            temp = []

        if s in exclude:
            s = sh.next()
            while s not in exclude:
                temp.append(s)
                s = sh.next()
            yield codons - set(temp)
            temp = []


def protein_motif(shorthand):
    ''' Returns a regex object useful for matching a protein motif. '''
    shortset = list(_protein_motif(shorthand))
    s = len(shortset)

    return s, re.compile('(?<=(' + ''.join(['[{}]'.format('|'.join(i))
                               for i in shortset]) + '))')
