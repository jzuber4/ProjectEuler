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
Private generator that returns successive Prime Numbers
Uses an expanding Eratosthenes Sieve
"""
def _PrimeNumbers():
    is_prime = [False]
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

prime_numbers = []
prime_number_gen = _PrimeNumbers()

# public prime number generator
# uses stored prime numbers
def PrimeNumbers():
    curr = 0
    while True:
        if curr == len(prime_numbers):
            prime_numbers.append(prime_number_gen.next())
        yield prime_numbers[curr]
        curr += 1


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
        if p * p > N:
            factors.append(N)
            break

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

# http://math.stackexchange.com/questions/22721/is-there-a-formula-to-calculate-the-sum-of-all-proper-divisors-of-a-number?rq=1
def SumOfProperDivisors(N):
    factors = PrimeFactors(N)
    count = 0
    last_factor = 0
    this_term = 1
    prod = 1

    # 2^3 * 3 * 5 => (1 + 2^1 + 2^2 + 2^3) * (1 + 3) * (1 + 5)
    # add up powers of a factor as its multiplicity is counted up
    # multiply that sum into the product
    for f in factors:
        if last_factor == f:
            # increase the term
            count += 1
            this_term += f ** count
        else:
            # multiply in the term, start new term
            prod *= this_term
            count = 1
            this_term = 1 + f
            last_factor = f
    prod *= this_term

    return prod - N




