"""
Problem 18: Maximum path sum I
Finds the maximum sum of a path through a triangle read from an input file
The input file defaults to Problem18.txt and must be run from the same
directory if that is the case.
usage:
python Problem18.py [input = Problem18.txt]
"""
import sys

def main():
    f = None
    try:
        f = open(sys.argv[1]) if len(sys.argv) > 1 else open("Problem18.txt")
    except:
        print "usage: python Problem18.py [input = Problem18.txt]"
        print ("The input file defaults to Problem18.txt and must be run from "
            + "the same directory if that is the case.")
        return

    lines = []
    for l in f:
        lines.append([int(i) for i in l.split()])

    # find paths in topological order
    for row, line in enumerate(lines):
        if row == 0: # skip first
            continue

        # max line to a point in the row is maximum of its two parents plus its value
        for column, value in enumerate(line):
            if column == 0:
                lines[row][column] += lines[row-1][column]
            elif column == len(line) - 1:
                lines[row][column] += lines[row-1][column-1]
            else:
                lines[row][column] += max(lines[row-1][column], lines[row-1][column-1])

    print max(lines[-1])

main()

