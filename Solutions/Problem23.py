"""
Problem 23: Non-abundant sums
Find the sum of all the positive integers which cannot be written
as the sum of two abundant numbers. All integers above 28123 can.
usage:
$ python Problem23.py
"""
from PEUtils import SumOfProperDivisors

def main():
    N = 28124
    abundants = []
    # calculate  abundants
    for i in xrange(1, N):
        if SumOfProperDivisors(i) > i:
            abundants.append(i)

    # mark numbers that are sums of abundants
    # python loops are slooooow ( < 1 sec before these loops, > 6 seconds after)
    has_sum = N * [False]
    for i in xrange(len(abundants)):
        a = abundants[i]
        for j in xrange(i + 1):
            b = abundants[j]

            if a + b >= N:
                break

            has_sum[a+b] = True

    print sum(i if not b
                else 0
                for i, b in enumerate(has_sum))

main()

