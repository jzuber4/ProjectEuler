"""
Problem 13: Large sum
Given a series of numbers from stdin, figure out the first k digits of input.
Increase precision (added digits considered) based on number of terms.
If k is not specified, it assumes the value of 10
If the input file is not specified, it assumes the value of "Problem13.txt"
If the input file is specified, k must also be specified before it
usage:
$ python Problem13.py [k = 10] [input = "Problem13.txt"]
"""
import sys
import math

def main():
    # read in
    k = 0
    f = None
    try:
        k = int(sys.argv[1]) if len(sys.argv) > 1 else 10
        f = open(sys.argv[2]) if len(sys.argv) > 2 else open("Problem13.txt")
    except:
        print "usage: python Problem13.py [k = 10] [input = \"Problem13.txt\"]"
        print ("If the input file is given, k must be given before it.\n"
            + "If the input file is not specified, the program must be run in"
            + " the same directory as Problem13.txt")
        return

    terms = []
    for l in f:
        terms.append(l)

    # number of terms determines how much precision we need
    number_of_terms = len(terms)
    num_digits = k + 1 + int(math.log(number_of_terms, 10))

    # perform the addition with a reduced number of digits
    truncated = sum(int(t[:num_digits]) for t in terms)

    print str(truncated)[:k]

main()

