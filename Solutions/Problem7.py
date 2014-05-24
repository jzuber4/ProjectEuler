# Problem 7: 10001st Prime
# Finds the Nth prime number
# usage:
# $ python Problem7.py N
from PEUtils import PrimeNumbers
import sys

def main():
    N = int(sys.argv[1])

    # use generator from PEUtils
    primes = PrimeNumbers()
    p = 0
    for i in range(N):
        p = primes.next()

    print p

main()


