def even_fib():

    '''
    Create a function to 
    '''
    accum = []

    for i in range(1, 3):
        accum.append(i)

    while sum(accum) < 4000000:
        accum.append(accum[-1] + accum[-2])

    return accum

print(even_fib())