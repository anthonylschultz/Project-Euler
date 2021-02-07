def py_trip():
    '''
    1) create function to see if a2 + b2 = c2
    2) create function to loop through numbers and calculate a2 + b2, check if == c2, accumulate a, b, c
    3) for accumulated values, check if sum == 1000
    '''
    def is_py():
        if (a**2) + (b**2) == (c**2):
            return True


    accum = []

    for a in range(1, 500):
        for b in range(1, 500):
            for c in range(1, 500):
                if a < b < c and is_py():
                    accum.append([a, b, c])

    accum_sums = []
    for lst in accum:
        if sum(lst) == 1000:
            accum_sums.append(lst)
    
    product = 1
    for i in accum_sums:
        for val in i:
            product *= val
    
    return product


print(py_trip())