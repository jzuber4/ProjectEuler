"""
Problem 15: Lattice paths
Starting in the top corner of an n x m grid, only being able to move right and down
how many paths are there? Equates to (n + m)! / (n! * m!),
there are n + m total moves to make, across which n elements must be chosen,
the remaining amount being m
usage:
$ python Problem15.py [n = 20] [m = n]
"""
import sys

def Factorial(x):
    val = 1
    for i in range(1, x+1):
        val *= i
    return val

def squared(x):
    return x * x

def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    m = int(sys.argv[2]) if len(sys.argv) > 2 else n

    print Factorial(n + m) / (Factorial(n) * Factorial(m))

main()
