"""
Problem 25: 1000-digit Fibonacci number
There is a closed form solution, but brute is ok here
Find the first Fibonacci number with N digits
N defaults to 1000
usage:
$ python Problem25.py [N = 1000]
"""
from PEUtils import Fibonacci, OptionalArg

def main():
    N = int(OptionalArg(0, 1000))
    for i, f in enumerate(Fibonacci()):
        if len(str(f)) >= N:
            print i
            break

main()
