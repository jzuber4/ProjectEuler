"""
Problem 24: Lexicographic permutations
(Particularly happy with this one :) )
Returns the Nth permutation of numbers 0 through k-1
N defaults to 1 million, k defaults to 10
If k is specified, N must be specified first
usage:
$ python Problem24.py [N = 1000000, k = 10]
"""
import sys
def Factorial(x):
    val = 1
    for i in range(1, x):
        val *= i
    return val

def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 1000000
    k = int(sys.argv[2]) if len(sys.argv) > 2 else 10

    # bag of remaining digits
    bag = [i for i in range(k)]
    # final permutation
    final = []
    # index of final permutation
    index = 0
    # remaining number of permutations
    remaining = N
    # precompute factorials
    factorials = [Factorial(i) for i in range(1, k+1)]

    # while there are remaining permutations
    while len(bag) > 0:
        count = 0
        count_num = 0
        # increasing the position of the bag of the number at index in final skips through
        # factorial(k - index - 1) permutations
        while count + factorials[k - index - 1] < remaining:
            count += factorials[k - index - 1]
            count_num += 1
        remaining -= count

        final.append(bag[count_num])
        bag.remove(bag[count_num])
        index += 1

    final_str = [str(s) for s in final]
    print reduce(lambda s, i: s + i, final_str)

main()
