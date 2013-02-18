def iev(genotypes):
    ''' Given: Six positive integers, each of which does not 
    exceed 20,000. The integers correspond to the number of 
    couples in a population possessing each genotype pairing 
    for a given factor. In order, the six given integers 
    represent the number of couples having the following genotypes:

    AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa-aa

    Return: The expected number of offspring displaying the dominant 
    phenotype in the next generation, under the assumption that every 
    couple has exactly two offspring.
    
    >>> iev([1, 0, 0, 1, 0, 1])
    3.5
    '''
    # d = dominant, h = hetrogeneous, r = reccesive
    dd = 1.0
    dh = 1.0
    dr = 1.0
    hh = 0.75
    hr = 0.50
    rr = 0.0
    
    coefficients = [dd, dh, dr, hh, hr, rr]
    children = [2*x*y for x, y in zip(genotypes, coefficients)]
    return sum(children)