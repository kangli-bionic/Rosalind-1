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
