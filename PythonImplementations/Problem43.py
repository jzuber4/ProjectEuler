"""
    Problem 43:

    Problem Description:

    The number, 1406357289, is a 0 to 9 pandigital number because
    it is made up of each of the digits 0 to 9 in some order,
    but it also has a rather interesting sub-string divisibility property.

    Let d_1 be the 1st digit, d_2 be the 2nd digit, and so on.
    In this way, we note the following:

    d_2 * d_3 * d_4  = 406 is divisible by 2
    d_3 * d_4 * d_5  = 063 is divisible by 3
    d_4 * d_5 * d_6  = 635 is divisible by 5
    d_5 * d_6 * d_7  = 357 is divisible by 7
    d_6 * d_7 * d_8  = 572 is divisible by 11
    d_7 * d_8 * d_9  = 728 is divisible by 13
    d_8 * d_9 * d_10 = 289 is divisible by 17

    Find the sum of all 0 to 9 pandigital numbers with this property.

    Problem Solution:

    Recursively try all solutions, only exploring valid prefixes.

"""

def recurr(current, remaining):
    primes = [2,3,5,7,11,13,17]

    # test for divisibility
    length = len(str(current))
    if length >= 4:
        p = primes[length - 4]
        divisible = (current % 1000) / p * p == (current % 1000)
        if not divisible:
            return 0
        elif length == 10:
            return current

    # recurr and check sub sequences
    return sum(recurr(int(str(current) + str(remaining[i])),
                      remaining[:i] + remaining[i+1:])
               for i in range(len(remaining)))

def main():
    print sum(recurr(i, range(10)[:i] + range(10)[i+1:]) for i in range(10))

main()
