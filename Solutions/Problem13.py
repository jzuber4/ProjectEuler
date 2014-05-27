"""
Problem 13: Large sum
Given a series of numbers from stdin, figure out the first k digits of input.
Increase precision (added digits considered) based on number of terms.
usage:
$ python Problem13.py k < input.txt
"""
import sys
import math

def main():
    # read in
    k = int(sys.argv[1])
    terms = []
    for l in sys.stdin:
        terms.append(l)

    # number of terms determines how much precision we need
    number_of_terms = len(terms)
    num_digits = k + 1 + int(math.log(number_of_terms, 10))

    # perform the addition with a reduced number of digits
    truncated = sum(int(t[:num_digits]) for t in terms)

    print str(truncated)[:k]

main()

