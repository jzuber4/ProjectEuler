# Problem 9: Special Pythagorean Triplet
# If any exist, find the pythagorean triplet(s) a, b, c
# such that a^2 + b^2 = c^2 and a + b + c = N and print a * b * c
# if N is omitted, it assumes the value of 1000
# usage
# $ python Problem09.py [N = 1000]
from PEUtils import PythagoreanTriples
import sys

def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
    # fast method for pythagorean triples, this runs in less than 0.1 seconds
    for (a, b, c) in PythagoreanTriples(N):
        if a + b + c == N:
            print a * b * c

main()
