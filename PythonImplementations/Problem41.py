"""
    Problem 41:

    Problem Description:


    We shall say that an n-digit number is pandigital if it makes
    use of all the digits 1 to n exactly once. For example, 2143
    is a 4-digit pandigital and is also prime.

    What is the largest n-digit pandigital prime that exists?

    Problem Solution:
    Originally tested all pandigital numbers up to 1..9 (reasonable guess)
    for primality and return the largest one.

    (only need to test up to 1..7)

"""
from PEUtils import IsPrime
from itertools import permutations

def is_pandigital(num):
    s = set(range(1,len(str(num)) + 1))
    return s == set(str(num))

def main():
    best = 0
    # test all pandigitals up to 1..9 for primality
    for i in range(2,10):
        for p in permutations(str(n) for n in range(1,i+1)):
            num = int("".join(p))
            if IsPrime(num):
                best = num
    print best

main()
