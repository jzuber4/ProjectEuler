# Problem 3: Largest Prime Factor
# find the largest prime factor of a number

# usage:
# $ python Problem3.py N
from PEUtils import PrimeFactors
import sys

# use the PrimeFactors function defined in PEUtils
def main():
    print max(PrimeFactors(int(sys.argv[1])))

main()
