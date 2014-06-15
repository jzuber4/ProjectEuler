"""
Problem 27:

Problem Description:
Euler discovered the remarkable quadratic formula:

    n^2 + n + 41

    It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

    The incredible formula n^2 - 79 n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, -79 and 1601, is -126479.

    Considering quadratics of the form:

    n^2 + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |-4| = 4
    Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

Solution:
First I filter potential b's to only the primes under the limit (in this case 1000),
then I try all pairs of a's and qualifying b's.

"""

from PEUtils import OptionalArg, PrimeNumbers
from PEUtils import IsPrime
from itertools import takewhile


def main():
    a_limit = int(OptionalArg(0, 1000))
    b_limit = int(OptionalArg(1, 1000))

    best_n = best_a = best_b = 0
    # for all prime numbers below b_limit
    for b_unsigned in takewhile(lambda p: p < b_limit, PrimeNumbers()):
        for b in [-b_unsigned, b_unsigned]:
            # for all a below a_limit
            for a in range(-a_limit + 1, a_limit):
                n = 0
                # while n counting from 0 is prime
                while IsPrime(n * n + a * n + b):
                    n += 1

                if n > best_n:
                    best_n = n
                    best_a = a
                    best_b = b

    print best_a * best_b

main()



