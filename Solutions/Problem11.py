"""
Problem 11: Largest product in a grid
Find the largest product of k numbers in a row in a grid read from an input file
If k is not specified, it assumes the value of 4
If the input file is not specified, it assumes the value of "Problem11.txt"
If the input file is specified, k must also be specified before it
usage:
$ python Problem11.py [k = 4] [input = "Problem11.txt"]
"""
import sys

"""
Multiply along grid recursively, returning 0 if out of bounds
position is x, y
remaining steps is k
next position is delta_x + x, delta_y + y
"""
def Look(lines, k, x, y, delta_x, delta_y):
    # check if out of bounds
    if y == 0 or y == len(lines) or x == 0 or x == len(lines[y]):
        return 0
    # done multiplying
    if k == 0:
        return 1

    return lines[y][x] * Look(lines, k-1,
                              x + delta_x, y + delta_y,
                              delta_x, delta_y)


def main():
    k = 0
    f = None
    try:
        k = int(sys.argv[1]) if len(sys.argv) > 1 else 4
        f = open(sys.argv[2]) if len(sys.argv) > 2 else open("Problem11.txt")
    except:
        print "usage: python Problem11.py [k = 4] [input = \"Problem11.txt\"]"
        print ("If the input file is given, k must be given before it.\n"
            + "If the input file is not specified, the program must be run in"
            + " the same directory as Problem11.txt")
        return

    lines = []
    # read in
    for l in f:
        lines.append([int(v) for v in l.split()])

    h = len(lines)
    w = len(lines[0])

    max_prod = 0
    # for each starting location, look each direction
    for j in range(h):
        for i in range(w):
            max_prod = max(max_prod,
                        max(Look(lines, k, i, j, 1,  0),
                        max(Look(lines, k, i, j, 0, -1),
                        max(Look(lines, k, i, j, 1, -1),
                            Look(lines, k, i, j, 1,  1)))))

    print max_prod

main()
