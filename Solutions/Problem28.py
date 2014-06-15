"""
Problem 28:

Problem Descrption:
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

Solution Description:
The sum of the corners at the square of size n > 1 is simply:
    4 times the area of the square (imagine all corners are the top right number)
    minus 6 times the one less than the length of a side
        (1 time for the top right, 2 times for the bottom left, 3 times for the bottom right)
Simply count up to n = 1001 for each odd n > 1 and sum these values and add 1 (for the center number)
"""
from PEUtils import OptionalArg

def main():
    n = int(OptionalArg(0, 1001))

    print 1 + sum(4 * i * i - 6 * (i - 1) for i in xrange(3, n + 1, 2))

main()
