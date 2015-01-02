"""
    Problem 39:

    Problem Description:

    If p is the perimeter of a right angle triangle with integral length sides,
    {a,b,c}, there are exactly three solutions for p = 120.

    {20,48,52}, {24,45,51}, {30,40,50}

    For which value of p <= 1000, is the number of solutions maximised?

    Problem Solution:
    Find most common perimeter by trying all eligible pythagorean triplets.
"""
from PEUtils import PythagoreanTriples

def main():
    # get list of perimeters of all eligible triangles
    lst = [a + b + c for (a, b, c) in PythagoreanTriples(1000) if a + b + c < 1000]
    # get most common perimeter: http://stackoverflow.com/a/1518632
    print max(set(lst), key=lst.count)

main()
