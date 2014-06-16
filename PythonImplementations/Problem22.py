"""
Problem 22: Names scores
Given a ascii file storing names in uppercase, surrounded by
quotation marks and separated by commas, calculate
the sum of the name scores for each name in the file.
The name score of a name is the product of the index of that name
in a sorted version of the file (indexed from 1) and the sum of
the position of its letters in the alphabet (index from 1 at A).
The ascii file defaults to Problem22.txt and must be run in the
same directory if that is the case.
usage:
python Problem22.py [input = Problem22.txt]
"""
import sys

def main():
    f = None
    try:
        f = open(sys.argv[1]) if len(sys.argv) > 1 else open("Problem22.txt")
    except:
        print "usage: python Problem22.py [input = Problem22.txt]"
        print ("The ascii file defaults to Problem22.txt and must be run in the"
              + "same directory if that is the case.")
        return

    # read from file, remove commas and quotations
    names = sorted(f.read().replace('"', '').split(','))

    # sum of indices multiplied by sum of character index from A
    print sum((index + 1) * sum(ord(c) - ord('A') + 1 for c in name) for index, name in enumerate(names))


main()
