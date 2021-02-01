def x_prime(x):
    '''
    get xth prime number
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

    val = 2

    primes = []

    while len(primes) != x:
        if is_prime(val):
            primes.append(val)
        val += 1

    for idx, prime_val in enumerate(primes, 1):
        print(f'#{idx}, Prime Value: {prime_val}')


print(x_prime(1000))