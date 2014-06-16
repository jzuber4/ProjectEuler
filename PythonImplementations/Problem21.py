"""
Problem 21: Amicable Numbers
Returns the sum of all the amicable numbers under N.
N defaults to 10000.
usage:
$ python Problem21.py [N = 10000]
"""
from PEUtils import SumOfProperDivisors
import sys

def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
    d = N * [0]
    for i in range(1, N):
        d[i] = SumOfProperDivisors(i)

    # sum up numbers that pass the amicable test
    print sum(i if d[i] < N and d[i] != i and d[d[i]] == i
                else 0
                for i in range(N))


main()
