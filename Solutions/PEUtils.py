"""
Generator that returns successive Fibonacci numbers,
starting with 0, then 1
"""
def Fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b

"""
Generator that returns successive Prime Numbers
Uses an expanding Eratosthenes Sieve
"""
def PrimeNumbers():
    # start with length of 4 (doubled to be 8)
    is_prime = 4 * [False]
    # first prime is 2
    primes = [2]
    # first number tested is 3
    highest = 3

    yield 2
    while True:
        # double length of array
        is_prime = [True] * 2 * len(is_prime)
        for i in primes:
            # calculate starting number
            curr = (highest / i) * i
            if curr < highest:
                curr += i

            # mark all divisible numbers as not prime
            while curr < highest + len(is_prime):
                is_prime[curr - highest] = False
                curr += i

        # count True slots as prime
        for i, v in enumerate(is_prime):
            if v:
                primes.append(i + highest)
                yield i + highest

"""
Return a list of the prime factors of N in sorted order.
Each factor appears a number of times equal to its multiplicity.
Ex:
PrimeFactors(360) => [2, 2, 2, 3, 3, 5]
PrimeFactors(11) => [11]
PrimeFactors(1) => []  // no prime factors
"""
def PrimeFactors(N):
    # get successive primes
    primes = PrimeNumbers()
    factors = []
    while N > 1:
        p = primes.next()

        # divide by a number of times equal to its multiplicity
        while N % p == 0:
            factors.append(p)
            N /= p

    return factors

# assumes column and row are same length
def DotProduct(column, row):
    return sum(i * j for (i,j) in zip(column, row))


# http://stackoverflow.com/questions/575117/generating-unique-ordered-pythagorean-triplets
def PythagoreanPrimitiveTriples(max_c):
    # matrices
    # inner lists are rows
    U = [[ 1, -2, 2], [ 2, -1, 2], [ 2, -2, 3]]
    A = [[ 1,  2, 2], [ 2,  1, 2], [ 2,  2, 3]]
    D = [[-1,  2, 2], [-2,  1, 2], [-2,  2, 3]]
    # most simple pythagorean triple
    m = [[3, 4, 5]]
    while m:
        for triple in m:
            yield triple
        g = ([DotProduct(column, row) for row in matrix] for column in m for matrix in (U, A, D))
        m = [i for i in g if i[2] <= max_c]

def PythagoreanTriples(max_c):
    for primitive in PythagoreanPrimitiveTriples(max_c):
        i = primitive[:]
        while i[2] <= max_c:
            yield i
            i = [i+j for (i,j) in zip(i, primitive)]


