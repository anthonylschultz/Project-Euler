def fib(length):
    '''
    Create function to return 20 iterations of the fibonacci sequence

    Parameter: length (int)
    Returns: List of length with fibonacci values
    '''

    count = 0
    a = 0
    b = 1

    fibs = [a, b]
    while count <= length:
        
        c = a + b
        fibs.append(c)

        a = b
        b = c
        
        count += 1

    return fibs



print(fib(length=20))