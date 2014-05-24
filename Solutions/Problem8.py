# Problem 8: Largest product in a series
# Find the largest product of k digits in a series of digits
# read from stdin
# usage:
# $ python Problem8.py k < input
import sys

def main():
    k = int(sys.argv[1])
    # read from stdin, remove newlines
    l = "".join(sys.stdin.read().split("\n"))
    nums = []
    for i in l:
        nums.append(int(i))

    # find consecutive products
    num_factors = 0
    prod = 1
    max_prod = 0
    for i in range(len(nums)):
        # if a zero is found, that can't be in the product
        # skip ahead
        if nums[i] == 0:
            num_factors = 0
            prod = 1
            continue

        # multiply in new number
        prod *= nums[i]
        # if not enough factors, cannot be considered for maximum product
        if num_factors < k:
            num_factors += 1
        else:
            # enough factors, divide out old one
            prod /= nums[i - k]
            max_prod = max(max_prod, prod)

    print max_prod





main()
