def fibd(n, m):
    ''' Mortal Fibonacci Rabbits

    Given: Positive integers n?100 and m?20.

    Return: The total number of pairs of rabbits that will
    remain after the n-th month (n?100) if all rabbits live
    for m months (m?20).

    >>> fibd(6, 3)
    4
    '''
    matrix = [[0 for i in range(m)] for j in range(n)]
    matrix[0][0] = 1
    for i in xrange(1, n):
        for j in xrange(1, m):
            matrix[i][j] = matrix[i-1][j-1]
        matrix[i][0] = sum(matrix[i-1][1:])
    return sum(matrix[-1])
