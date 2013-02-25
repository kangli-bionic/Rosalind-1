from rutility.utility import memoize

@memoize
def fib(n, k):
    ''' Rabbits and Recurrence Relations

    Given: Positive integers n?40 and k?5.

    Return: The total number of rabbit pairs that will be present 
    after n (n?36) months if each pair of reproduction-age rabbits 
    produces a litter of k (2?k?5) rabbit pairs in each generation 
    (instead of only 1 pair).
    
    >>> fib(5, 3)
    19'''
    if n < 2:
        return n
    else:
        return fib(n-1, k) + (k * fib(n-2, k))

