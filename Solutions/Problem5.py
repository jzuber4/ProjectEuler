# Problem 5: Smallest multiple
# find the smallest number is evenly divisible by integers 1 through N
# usage:
# $ python Problem5.py N
from PEUtils import PrimeFactors
import sys

# merge two lists
def merge(list_a, list_b):
    result = []
    curr_a = 0
    curr_b = 0

    # both indices in bounds
    while curr_a < len(list_a) and curr_b < len(list_b):
        # equal, move forward on both
        if list_a[curr_a] == list_b[curr_b]:
            result.append(list_a[curr_a])
            curr_a += 1
            curr_b += 1
        # inequal cases: move one forward
        elif list_a[curr_a] < list_b[curr_b]:
            result.append(list_a[curr_a])
            curr_a += 1
        elif list_a[curr_a] > list_b[curr_b]:
            result.append(list_b[curr_b])
            curr_b += 1

    # rest of list_a
    while curr_a < len(list_a):
        result.append(list_a[curr_a])
        curr_a += 1

    # rest of list_b
    while curr_b < len(list_b):
        result.append(list_b[curr_b])
        curr_b += 1

    return result


def main():
    N = int(sys.argv[1])
    factors = []
    # get common factors of numbers 2 through N + 1
    for i in range(2, N + 1):
        # merge to find common factors
        factors = merge(factors, PrimeFactors(i))

    # product of common factors is lowest number that all evenly divide
    v = 1
    for f in factors:
        v *= f

    print v

main()
