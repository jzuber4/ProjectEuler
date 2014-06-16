"""
Problem 16: Power digit sum
Prints the sum of the digits of the number N
N defaults to 2**1000
usage:
python Problem16.py [N = 2**1000]
"""
import sys

def main():
    N = sys.argv[1] if len(sys.argv) > 1 else str(2 ** 1000)
    print sum(int(i) for i in N)

main()
