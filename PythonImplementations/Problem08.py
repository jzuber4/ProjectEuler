# Problem 8: Largest product in a series
# Find the largest product of k digits in a series of digits
# read from an input file
# k defaults to 13, input file defaults to Problem08.txt
# Must have either 0 or 2 arguments, must be run in current directory if arguments omitted
# usage:
# $ python Problem08.py [k = 13] [input = Problem08.txt]
import sys

def main():
    k = 0
    f = None
    try:
        k = int(sys.argv[1]) if len(sys.argv) > 1 else 13
        f = open(sys.argv[2]) if len(sys.argv) > 2 else open("Problem08.txt")
    except:
        print "usage: python Problem08.py [k = 13] [input = \"Problem08.txt\"]"
        print ("If the input file is given, k must be given before it.\n"
            + "If the input file is not specified, the program must be run in"
            + " the same directory as Problem08.txt")
        return


    # read from stdin, remove newlines
    l = "".join(f.read().split("\n"))
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
