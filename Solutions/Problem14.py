"""
Problem 14: Longest Collatz Sequence
Finds the number under N > 1 with the longest collatz sequence
Saves old results to prevent recomputations
usage:
$ python Problem14.py N
"""
import sys


# store old collatz lengths for efficiency
collatz_lengths = {}
def Collatz(n):
    # base case
    if n == 1:
        return 0

    # recurse through sequence to find length
    if not n in collatz_lengths:
        next_collatz = n / 2 if n % 2 == 0 else 3 * n + 1
        collatz_lengths[n] = 1 + Collatz(next_collatz)

    return collatz_lengths[n]

def main():
    N = int(sys.argv[1])

    # try all numbers from 1 to N
    max_collatz = 0
    max_i = 1
    for i in range(1, N):
        curr_collatz = Collatz(i)
        if curr_collatz > max_collatz:
            max_i = i
            max_collatz = curr_collatz

    print max_i

main()
