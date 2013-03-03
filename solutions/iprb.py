from itertools import product


def iprb(d, h, r):
    ''' Mendel's First Law

    Given: Three positive integers k, m, and n, representing a
    population containing d+h+r organisms:
    d - homozygous dominant
    h - heterozygous
    r - homozygous recessive

    Return: The probability that two randomly selected mating organisms
    will produce an individual possessing a dominant allele (and thus
    displaying the dominant phenotype). Assume that any two organisms can mate.

    >>> round(iprb(2, 2, 2), 5)
    0.78333
    '''
    total = float(sum((d, h, r)))

    dd = d/total * (d-1)/(total-1)
    hd = d/total * (h)/(total-1)
    rd = d/total * (r)/(total-1)

    dh = h/total * (d)/(total-1)
    hh = h/total * (h-1)/(total-1)
    rh = h/total * (r)/(total-1)

    dr = r/total * (d)/(total-1)
    hr = r/total * (h)/(total-1)
    rr = r/total * (r-1)/(total-1)

    matrix = [dd, hd, rd,
              dh, hh, rh,
              dr, hr, rr]

    coefficients = [1.0, 1.0,  1.0,
                    1.0, 0.75, 0.5,
                    1.0, 0.5,  0.0]

    # matrix:
    #
    #     d   h   r
    # d  dd  hd  rd     dd == 100%    hh == 50%
    # h  dh  hh  rh     hd == 100%    hr == 25%
    # r  dr  hr  rr     rd == 100%    rr ==  0%
    # to display the dominant phenotypes,
    # multiply by the coefficients, and sum the array.

    return sum(x * y for x, y in zip(coefficients, matrix))
