"""
Problem 12: Highly divisible triangular number
Calculates the first triangular number with over N divisors
If N is omitted, it assumes the value of 500
usage:
$ python Problem12.py [N = 500]
"""
from PEUtils import PrimeFactors, PrimeNumbers
import sys

# returns the number of divisors for a number N
def NumberOfDivisors(N):
    # Factor the number
    factors = PrimeFactors(N)
    last_factor = 0
    factor_count = 1

    # get multiplicities
    factor_counts = []
    for factor in factors:
        if factor != last_factor:
            factor_counts.append(1)
            last_factor = factor
        else:
            factor_counts[-1] += 1

    # multiply them
    divisor_prod = 1
    for count in factor_counts:
        divisor_prod *= 1 + count

    return divisor_prod

def TriangleNumber(n):
    return ((n + 1) * n) / 2

def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 500
    num_divisors = 0
    i = 0
    while num_divisors <= N:
        i += 1
        # formula for triangle numbers (N+1 choose 2)
        triangle_num = TriangleNumber(i)

        num_divisors = NumberOfDivisors(triangle_num)

    print TriangleNumber(i)

main()

