import os
import solutions
import rutility
from rutility.fileops import lineoutput
from rutility.fileops import listoutput
from rutility.fileops import readfile

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
    from rutility.parsers import fasta
    f = readfile('rosalind_gc.txt')
    with f:
        iterfasta = fasta(f)
        result = max(iterfasta, key=gc)
        lineoutput(result.name)
        lineoutput(gc(result))


def problem_hamm():
    ''' http://rosalind.info/problems/hamm/ '''
    from solutions.hamm import hamm
    f = readfile('rosalind_hamm.txt')
    with f:
        s, t = f.next(), f.next()
        lineoutput(hamm(s, t))


def problem_iprb():
    ''' http://rosalind.info/problems/iprb/ '''
    from solutions.iprb import iprb
    f = readfile('rosalind_iprb.txt')
    with f:
        d, h, r = [int(i) for i in f.next().split()]
        lineoutput(iprb(d, h, r))


def problem_prot():
    ''' http://rosalind.info/problems/prot/ '''
    from solutions.prot import prot
    f = readfile('rosalind_prot.txt')
    with f:
        for line in f:
            lineoutput(prot(line))


def problem_subs():
    ''' http://rosalind.info/problems/subs/ '''
    from solutions.subs import subs
    f = readfile('rosalind_subs.txt')
    with f:
        dna, sub = f.next(), f.next()
        listoutput(subs(dna, sub))


def problem_cons():
    ''' http://rosalind.info/problems/cons/ '''
    from solutions.cons import cons
    from rutility.parsers import fasta
    f = readfile('rosalind_cons.txt')
    with f:
        iterfasta = fasta(f)
        collection = [i.data for i in iterfasta]
        consensus, matrix = cons(collection)
        lineoutput(consensus)
        listoutput(matrix[0], prefix='A: ')
        listoutput(matrix[1], prefix='C: ')
        listoutput(matrix[2], prefix='G: ')
        listoutput(matrix[3], prefix='T: ')


def problem_perm():
    ''' http://rosalind.info/problems/perm/ '''
    from solutions.perm import perm
    f = readfile('rosalind_perm.txt')
    with f:
        n = int(f.next())
        total, perms = perm(n)
        lineoutput(total)
        for p in perms:
            listoutput(p)


def problem_grph():
    ''' http://rosalind.info/problems/grph/ '''
    from solutions.grph import grph
    from rutility.parsers import fasta
    f = readfile('rosalind_grph.txt')
    with f:
        iterfasta = fasta(f)
        gs = grph(iterfasta, 3)
        for g in gs:
            listoutput(g)


def problem_iev():
    ''' http://rosalind.info/problems/iev/ '''
    from solutions.iev import iev
    f = readfile('rosalind_iev.txt')
    with f:
        lineoutput(iev([int(i) for i in f.next().split()]))


def problem_fib():
    ''' http://rosalind.info/problems/fib/ '''
    from solutions.fib import fib
    f = readfile('rosalind_fib.txt')
    with f:
        n, k = [int(i) for i in f.next().split()]
        lineoutput(fib(n, k))


def problem_lcsm():
    ''' http://rosalind.info/problems/lcsm/ '''
    from solutions.lcsm import lcsm
    from rutility.parsers import fasta
    f = readfile('rosalind_lcsm.txt')
    with f:
        iterfasta = fasta(f)
        collection = [i.data for i in iterfasta]
        lineoutput(lcsm(collection))


def problem_lia():
    ''' http://rosalind.info/problems/lia/ '''
    from solutions.lia import lia
    f = readfile('rosalind_lia.txt')
    with f:
        k, n = [int(i) for i in f.next().split()]
        lineoutput(lia(k, n))


def problem_mprt():
    ''' http://rosalind.info/problems/mprt/ '''
    from solutions.mprt import mprt
    from rutility.parsers import uniprot
    f = readfile('rosalind_mprt.txt')
    with f:
        for line in f:
            prot = uniprot(line.strip())
            locations = mprt(prot.data, 'N{P}[ST]{P}')
            if locations:
                lineoutput(line.strip())
                listoutput(locations)


def problem_fibd():
    ''' http://rosalind.info/problems/fibd/ '''
    from solutions.fibd import fibd
    f = readfile('rosalind_fibd.txt')
    with f:
        m, n = [int(i) for i in f.next().split()]
        lineoutput(fibd(m, n))