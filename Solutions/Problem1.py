# Problem 1: Multiples of 3 and 5
# print the sum of integers less than 1000 divisble by 3 or 5
# there also exists a closed form solution
# usage:
# $ python Problem1.py
def main():
    val = 0

    # loop over all numbers and keep summing
    for i in range (1000):
        if i % 3 == 0 or i % 5 == 0:
            val += i

    print val

main()
