"""
    Problem 35:

    Problem Definition:
    The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

    There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

    How many circular primes are there below one million?

    Problem Solution:
    Given an efficient prime checker, this is not very hard!
"""
from PEUtils import PrimeNumbers, IsPrime, OptionalArg
from itertools import takewhile

# takes n and returns whether all rotations of n are prime
def isCircularPrime(n):
    string = str(n)

    # at each index, split string
    for index in range(len(string)):
        rotated = string[index:] + string[:index]
        if not IsPrime(int(rotated)):
            return False

    return True


def main():
    N = int(OptionalArg(0, 1000000))

    # precompute all primes in range, lookup to determine primality
    primes = takewhile(lambda x: x < N, PrimeNumbers())

    print sum(1 for p in primes if isCircularPrime(p))


main()
