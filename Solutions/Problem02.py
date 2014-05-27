# Problem 2: Even Fibonacci Numbers
# find the sum of the even fibonacci numbers less than N
# if N is omitted, 4 million is used
# usage:
# $ python Problem02.py [N = 4000000]
from PEUtils import Fibonacci
import sys

def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 4000000

    # use the Fibonacci generator in PEUtils
    f = Fibonacci()
    v = f.next()
    sum_val = 0

    while v < N:
        if v % 2 == 0:
            sum_val += v
        v = f.next()

    print sum_val

main()

