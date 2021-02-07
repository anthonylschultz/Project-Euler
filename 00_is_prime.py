def is_prime(x):
    '''
    1) list all factors of number
    2) if number of factors equal 2 and factors are 1 and itself, = prime
    3) else: not prime
    returns: true/false if number is prime
    '''

    factors = []

    for i in range(1, x+1):
        if x % i == 0:
            factors.append(i)

    if len(factors) != 2:
        return 'Not a prime number'

    elif len(factors) == 2:
        return 'We have a prime number!'



print(is_prime(100))



