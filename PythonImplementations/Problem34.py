"""
    Problem 34:

    Problem Definition:
    145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

    Find the sum of all numbers which are equal to the sum of the factorial of their digits.

    Note: as 1! = 1 and 2! = 2 are not sums they are not included.

    Problem Solution:
    Brute Force! Try all values under 1 million.
"""

def main():
    # just store them all
    factorial = [1]
    for limit in range(1, 10):
        factorial.append(reduce(lambda prod, f: prod * f, range(1,limit+1), 1))

    print sum(n for n in range(3, 1000000) if n == sum(factorial[int(c)] for c in str(n)))

main()
