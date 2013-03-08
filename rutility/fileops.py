import os


def readfile(filename):
    ''' Reads a file in the solution data directory.
    Returns a file object. '''
    f = open('data\%s' % filename)
    return f


def listoutput(data, prefix=''):
    ''' Prints a list in the rosalind output format.
    >>> listoutput((1, 2, 3))
    1 2 3
    >>> listoutput([1, 2, 3])
    1 2 3
    >>> listoutput(xrange(1, 4))
    1 2 3
    >>> listoutput(xrange(1, 11), "Watch me count! ")
    Watch me count! 1 2 3 4 5 6 7 8 9 10
    '''
    print '{}{}'.format(prefix, " ".join([str(i) for i in data]))


def lineoutput(data, prefix=''):
    ''' Prints a line in the rosalind output format.
    >>> lineoutput(1)
    1
    >>> lineoutput(1, "Note the space! ")
    Note the space! 1
    >>> lineoutput(1, "No space!")
    No space!1
    '''
    print '{}{}'.format(prefix, data)


def getfiles(d, ext):
    ''' Gets all *.ext files in a directory, recursively '''
    for r, d, f in os.walk(d):
        for files in f:
            if files.endswith('.%s' % ext):
                print os.path.join(r, files)
