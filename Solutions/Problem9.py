# Problem 9: Special Pythagorean Triplet
# find the pythagorean triplet a, b, c
# such that a^2 + b^2 = c^2 and a + b + c = 1000
# and print a * b * c
# usage
# $ python Problem9.py
from PEUtils import PythagoreanTriples

def main():
    # fast method for pythagorean triples, this runs in less than 0.1 seconds
    for (a, b, c) in PythagoreanTriples(1000):
        if a + b + c == 1000:
            print a * b * c

main()
