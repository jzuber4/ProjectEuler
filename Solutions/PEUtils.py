def Fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b

def PrimeNumbers():
    is_prime = [False, False, True]
    primes = [2]
    highest = 3
    yield 2
    while True:
        is_prime = [True] * 2 * len(is_prime)
        for i in primes:
            curr = (highest / i) * i
            if curr < highest:
                curr += i

            while curr < highest + len(is_prime):
                is_prime[curr - highest] = False
                curr += i

        for i, v in enumerate(is_prime):
            if v:
                primes.append(i + highest)
                yield i + highest

def PrimeFactors(N):
    primes = PrimeNumbers()
    factors = []
    while N > 1:
        p = primes.next()

        if p > N:
            factors.append(p)
            break

        while N % p == 0:
            factors.append(p)
            N /= p

    return factors






