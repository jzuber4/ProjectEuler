"""
    Problem 30:
    Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4
    As 1 = 1^4 is not a sum it is not included.

    The sum of these numbers is 1634 + 8208 + 9474 = 19316.

    Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

    Solution Description:
    9 is the possible value for any digit. Taking a conservative estimate that all sums are below
    360000 (since 6 * 9^5 is much less than 999,999 and grows much less fast than adding more 9s)
    and trying all possible values readily gives the answer. A more clever solution definitely exists
    but this runs very fast.

"""
def main():
    print sum(n for n in range(2, 360000)
                 if n == sum(int(i) ** 5 for i in str(n)))

main()
