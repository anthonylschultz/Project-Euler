def py_trip():

    a = 0
    b = 1

    a_s = []
    b_s = []
    c_s = []

    for val in range(0, 1000):
        c = (a**2 + b**2)
        

        a_s.append(a)
        b_s.append(b)
        c_s.append(c)



        a += 1
        b += 1


    for a, b, c in zip(a_s, b_s, c_s):
        if (a**2) + (b**2) == (c**2):
            print(a, b, c)


    # return [a_s, b_s, c_s]


    '''
    1) calculate a**2 + b**2 = c**2 (0, 100)
    2) pack a, b, c values into object
    '''

print(py_trip())