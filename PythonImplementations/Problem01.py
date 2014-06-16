# Problem 1: Multiples of 3 and 5
# print the sum of integers less than N divisible by 3 or 5
# there also exists a closed form solution
# if N is omitted, 1000 is used
# usage:
# $ python Problem01.py [N = 1000]
import sys

# use the PrimeFactors function defined in PEUtils
def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 1000

    print sum(i if i % 3 == 0 or i % 5 == 0
                else 0
                for i in range(N))

main()
