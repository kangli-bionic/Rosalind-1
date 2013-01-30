import os

import solutions
import rutility
from rutility import lineoutput
from rutility import listoutput
from rutility import readfile

# The datasets for project rosalind are randomly generated.
# The data file presented is therefore only one of many possible.

def problem_001():
    ''' http://rosalind.info/problems/dna/ '''
    from solutions.dna import dna
    f = readfile('rosalind_dna.txt')
    for line in f:
        listoutput(dna(line))

def problem_002():
    ''' http://rosalind.info/problems/rna/ '''
    from solutions.rna import rna
    f = readfile('rosalind_rna.txt')
    for line in f:
        lineoutput(rna(line))

def problem_003():
    ''' http://rosalind.info/problems/revc/ '''
    from solutions.revc import revc
    f = readfile('rosalind_revc.txt')
    for line in f:
        lineoutput(revc(line))

