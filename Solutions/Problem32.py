"""
    Problem 32:

    Problem Description:
    We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

    The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

    Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

    HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

    Problem Solution:
    Filtering by valid products could be hard, so I will start by filtering by number of digits.
    I will search for a, b such that 10 - digits(a) + digits(b) + digits(a*b) = 0
    digits(a*b) is at least digits(b) and will only increase as a gets larger

    the maximum b will be 9999 (since five digits would leave no room for a)
"""
from itertools import takewhile
# tests if all characters in a string are unique and none are '0'
def uniqueDigits(string):
    counts = set()
    for c in string:
        # illegal character
        if c == '0':
            return False
        # has already been seen (each needs to be unique)
        if c in counts:
            return False
        counts.add(c)

    return True

def main():
    products = set()

    for b in range(1, 10000):
        for a in range(1, b+1):
            c = a * b
            combinedString = str(a) + str(b) + str(c)

            # if all characters in the string are unique and nonzero and it has length 9
            # then it is nondigital
            if len(combinedString) == 9 and uniqueDigits(combinedString):
                products.add(c)
            elif len(combinedString) > 9:
                break

    print sum(products)

main()
