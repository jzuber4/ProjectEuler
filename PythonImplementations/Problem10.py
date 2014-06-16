# Problem 10: Summation of primes
# Find the sum of all primes below N
# if N is omitted, it assumes the value of 2 million
# usage:
# $ python Problem10.py [N = 2000000]
from PEUtils import PrimeNumbers
import sys

def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 2000000
    v = 0

    for p in PrimeNumbers():
        if p >= N:
            break
        v += p

    print v

main()
