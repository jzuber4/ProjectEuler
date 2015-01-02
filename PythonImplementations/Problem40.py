"""
    Problem 40:

    Problem Description:

    An irrational decimal fraction is created by concatenating the
    positive integers:

    0.123456789101112131415161718192021...

    It can be seen that the 12th digit of the fractional part is 1.

    If d_n represents the nth digit of the fractional part, find
    the value of the following expression.

    d_1 * d_10 * d_100 * d_1000 * d_10000 * d_100000 * d_1000000

    Problem Solution:
    Find the positive integer and the position in that integer
    given n to get the digit.
    The first 9 digits correspond to numbers 1..9
    The next 180 digits correspond to numbers 10..99
    The next (10**(i-1))*9*i digits correspond to numbers 10**(i-1)..10**(i)-1
    and so forth.

    Subtract away these terms until (10**(i-1))*9*i is greater than n
    Find the original positive number by getting the index of the positive
    number (grp) in the series given n and the number of digits at the current magnitude (i)
    Find the position of the digit (idx) in that number given n and the number of digits
    at the current magnitude (i).

    These can be used to find d(n)
    d(n) = the idxth digit of 10**(i-1) + grp


"""
from operator import mul

def d(n):
    # hardcode first 9
    if n < 10:
        return n

    # shift numbers over until first number of that
    # magnitude is first
    magnitude = 1
    while n > (10 ** (magnitude - 1)) * 9 * magnitude:
        n -= (10 ** (magnitude - 1)) * 9 * magnitude
        magnitude += 1
    # switch to 0 indexing
    n -= 1
    # the group is the position in the series of numbers at the
    # current magnitude
    # group (11) = 0 (the first number in the double digits -> 10)
    group = n / magnitude
    # index is the position in the number of the series
    # index(11) = 1 since the 11th digit is at index 1 of the number
    # it is in
    index = n % magnitude
    # add back the leading digit to the group to get the original
    # number of the series
    s = str(10 ** (magnitude - 1) + group)
    # index that number for the final digit
    return int(s[index])

def main():
    print reduce(mul, map(lambda i: d(10 ** i), range(0, 7)), 1)

main()
