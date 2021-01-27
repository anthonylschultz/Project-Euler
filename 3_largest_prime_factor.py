x = 88888
def prime_factors(x):
    '''
    0) list factors of x
    1) list prime factors of x
    2) get max value out of prime factors
    
    prime factor = 
    '''

    def is_prime(x):
        factors = []

        for i in range(1, x+1):
            if x % i == 0:
                factors.append(i)

        if len(factors) != 2:
            return False

        elif len(factors) == 2:
            return True

    num_factors = []

    for i in range(1, x+1):
        if x % i == 0:
            num_factors.append(i)

    prime_factors = []

    for val in num_factors:
        if is_prime(val):
            prime_factors.append(val)

    return max(prime_factors)

print(prime_factors(x))


