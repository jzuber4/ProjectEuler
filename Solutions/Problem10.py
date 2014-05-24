# Problem 10: Summation of primes
# Find the sum of all primes below N
# usage:
# $ python Problem10.py N
from PEUtils import PrimeNumbers
import sys

def main():
    N = int(sys.argv[1])
    v = 0

    for p in PrimeNumbers():
        if p >= N:
            break
        v += p

    print v

main()
