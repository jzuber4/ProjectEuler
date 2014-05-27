# Problem 6: Sum square difference
# Find the difference of the sum of the numbers from 1 to N squared
# and the sum of the squares of the numbers from 1 to N
# usage:
# $ python Problem06.py [N = 100]
import sys

def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 100

    # closed form solutions from WolframAlpha
    total = (n * (n + 1)) / 2
    sum_squared = total * total
    sum_of_squares = (n * (n + 1) * (2 * n + 1)) / 6


    print sum_squared - sum_of_squares


main()
