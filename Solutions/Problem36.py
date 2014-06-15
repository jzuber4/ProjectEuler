"""
    Problem 36:

    Problem Definition:
    The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

    Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

    (Please note that the palindromic number, in either base, may not include leading zeros.)

    Problem Solution:
    Simply try all odd numbers (since the first binary digit must be a 1)

"""
from PEUtils import OptionalArg

# returns a binary string of n
def toBinary(n):
    b_str = ""
    while n > 0:
        b_str += "1" if n % 2 else "0"
        n /= 2
    return b_str[::-1]

def isPalindrome(s):
    return s == s[::-1]

def main():
    N = int(OptionalArg(0, 1000000))
    print sum(n for n in range(1, N, 2)
            if isPalindrome(str(n)) and isPalindrome(toBinary(n)))


main()
