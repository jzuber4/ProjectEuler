"""
Problem 20: Factorial digit sum
Returns the sum of the digits in the factorial of N
N defaults to 100
usage:
$ python Problem20.py [N = 100]
"""
import sys

def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    print sum(int(i) for i in str(reduce(lambda prod, term: prod * term, range(1, N+1))))

main()
