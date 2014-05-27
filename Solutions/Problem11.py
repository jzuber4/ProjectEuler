"""
Problem 11: Largest product in a grid
Find the largest product of k numbers in a row in a grid read from stdin
usage:
$ python Problem11.py 4 < Problem11.txt
$ 70600674
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
    k = int(sys.argv[1])
    lines = []
    # read in
    for l in sys.stdin:
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
