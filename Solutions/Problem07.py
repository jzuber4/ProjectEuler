# Problem 7: 10001st Prime
# Finds the Nth prime number
# if N is omitted, 10001 is used
# usage:
# $ python Problem07.py [N = 10001]
from PEUtils import PrimeNumbers
import sys

def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 10001

    # use generator from PEUtils
    primes = PrimeNumbers()
    p = 0
    for i in range(N):
        p = primes.next()

    print p

main()


