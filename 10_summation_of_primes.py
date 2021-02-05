# sum all primes below two million

def sum_primes(var):
    def is_prime(x):
        factors = []

        for i in range(1, x+1):
            if x % i == 0:
                factors.append(i)

        if len(factors) != 2:
            return False

        elif len(factors) == 2:
            return True

    primes = []

    for i in range(1, var+1):
        if is_prime(i):
            primes.append(i)

    return sum(primes)

print(sum_primes(2000000))
