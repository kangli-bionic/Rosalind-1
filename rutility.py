import os
from collections import namedtuple

def readfile(filename):
    ''' Reads a file in the solution data directory. 
    Returns a file object. '''
    f = open('data\%s' % filename)
    return f

def listoutput(data):
    ''' Prints a list in the rosalind output format. '''
    print " ".join([str(i) for i in data])

def lineoutput(data):
    ''' Prints a line in the rosalind output format. '''
    print data

def getfiles(d, ext):
    ''' Gets all *.ext files in a directory, recursively '''
    for r, d, f in os.walk(d):
        for files in f:
            if files.endswith('.%s' % ext):
                print os.path.join(r, files)

Fasta = namedtuple("Fasta", "name, data")

def fasta(iterator):
    ''' Parses an iterator or file object into discrete fasta objects. '''
    name = iterator.next().strip()[1:]
    results = [iterator.next().strip()]
    item = iterator.next().strip()
    while True:
        if item[0] == ">":
            yield Fasta(name, "".join(results))
            results = [iterator.next().strip()]
            name, item = item[1:], iterator.next().strip()

        else:
            results.append(item)
            try:
                item = iterator.next().strip()
            except StopIteration:
                break
    yield Fasta(name, "".join(results))

def fastatest():
    ''' Test function for the fasta parser. 
    >>> fastatest()
    Fastatest pass!
    '''
    testdata = iter([i for i in """>Rosalind_6404
    CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
    TCCCACTAATAATTCTGAGG
    >Rosalind_5959
    CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
    ATATCCATTTGTCAGCAGACACGC
    >Rosalind_0808
    CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
    TGGGAACCTGCGGGCAGTAGGTGGAAT""".split('\n')])
    f = readfile('fastatest.txt')
    with f:
        tests = (fasta(testdata), fasta(f))  # hard coded test data, loaded test data
        for test in tests:
            a, b, c = test.next(), test.next(), test.next()
            assert a.name=='Rosalind_6404' and a.data=='CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG'
            assert b.name=='Rosalind_5959' and b.data=='CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC'
            assert c.name=='Rosalind_0808' and c.data=='CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT'

        print "Fastatest pass!"
