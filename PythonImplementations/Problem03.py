# Problem 3: Largest Prime Factor
# find the largest prime factor of a number
# if N is not specified, 600851475143 is used as N
# usage:
# $ python Problem03.py [N = 600851475143]
from PEUtils import PrimeFactors
import sys

# use the PrimeFactors function defined in PEUtils
def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 600851475143
    print max(PrimeFactors(N))

main()
