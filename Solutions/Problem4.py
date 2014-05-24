# Problem 4: Largest Palindrome Product
# Find the largest palindrome number that is a product of two three digit numbers
# usage:
# $ python Problem4.py
import sys

# helper function, returns true if number is palindrome, false if not
def isPalindrome(n):
    s = str(n)
    l = len(s)

    # only necessary to check front half against back hafl
    for i in range(l / 2):
        if s[i] != s[-i - 1]:
            return False

    return True

def main():
    max_val = 0

    # highest palindrome product most like in top 10% of two factors
    for i in range(900, 1000):
        for j in range(i, 1000):
            v = i * j
            if isPalindrome(v):
                max_val = max(v, max_val)

    print max_val

main()
