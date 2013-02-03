import os

import solutions
import rutility
from rutility import lineoutput
from rutility import listoutput
from rutility import readfile

# The datasets for project rosalind are randomly generated.
# The data file presented is therefore only one of many possible.

def problem_dna():
    ''' http://rosalind.info/problems/dna/ '''
    from solutions.dna import dna
    f = readfile('rosalind_dna.txt')
    with f:
        for line in f:
            listoutput(dna(line))

def problem_rna():
    ''' http://rosalind.info/problems/rna/ '''
    from solutions.rna import rna
    f = readfile('rosalind_rna.txt')
    with f:
        for line in f:
            lineoutput(rna(line))

def problem_revc():
    ''' http://rosalind.info/problems/revc/ '''
    from solutions.revc import revc
    f = readfile('rosalind_revc.txt')
    with f:
        for line in f:
            lineoutput(revc(line))

def problem_gc():
    ''' http://rosalind.info/problems/gc/ '''
    from solutions.gc import gc
    from rutility import fasta
    f = readfile('rosalind_gc.txt')
    with f:
        iterfasta = fasta(f)
        result = max(iterfasta, key=gc)
        lineoutput(result.name)
        lineoutput(gc(result))

