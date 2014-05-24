# Problem 6: Sum square difference
# Find the difference of the sum of the numbers from 1 to N squared
# and the sum of the squares of the numbers from 1 to N
# usage:
# $ python Problem6.py N
import sys

def main():
    N = int(sys.argv[1])
    sum_squared = sum_of_squares = 0

    # add up all the terms
    for i in range(N+1):
        sum_squared += i
        sum_of_squares += i * i

    sum_squared *= sum_squared

    print sum_squared - sum_of_squares


main()
