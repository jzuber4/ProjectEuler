"""
    Problem 37:

    Problem Description:
    The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

    Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

    NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

    Problem Solution:
    Continue until 11 primes are found
"""
from PEUtils import IsPrime, PrimeNumbers

# returns whether a given prime (not checked) is a truncatable prime
def IsTruncatablePrime(p):
    # excluded
    if p < 10:
        return False

    string = str(p)
    # test all truncations each direction
    for i in range(1, len(string)):
        if not IsPrime(int(string[i:])) \
            or not IsPrime(int(string[:i])):
            return False
    return True

def main():
    truncatable_primes = []

    # try all prime numbers
    for p in PrimeNumbers():
        if IsTruncatablePrime(p):
            # halt when enough have been reached
            truncatable_primes.append(p)
            if len(truncatable_primes) == 11:
                break

    print sum(truncatable_primes)

main()
