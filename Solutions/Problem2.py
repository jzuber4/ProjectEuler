# Problem 2: Even Fibonacci Numbers
# find the sum of the even fibonacci numbers less than 4 million
# usage:
# $ python Problem2.py
from PEUtils import Fibonacci

def main():
    # use the Fibonacci generator in PEUtils
    f = Fibonacci()
    v = f.next()
    sum_val = 0

    while v < 4000000:
        if v % 2 == 0:
            sum_val += v
        v = f.next()

    print sum_val

main()

