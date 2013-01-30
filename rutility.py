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