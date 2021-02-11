def power_digit(num, power):
    

    '''
    215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

    What is the sum of the digits of the number 21000?
    '''
    prod = num ** power

    lst_prod = list(str(prod))
    lst_prod = [int(i) for i in lst_prod]

    sum_ = 0

    for i in lst_prod:
        sum_ += i

    return sum_






print(power_digit(2, 1000))