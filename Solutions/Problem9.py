# Problem 9: Special Pythagorean Triplet
# find the pythagorean triplet a, b, c
# such that a^2 + b^2 = c^2 and a + b + c = 1000
# usage
# $ python Problem9.py

def main():
    # maximum i is 333
    for i in range(333):
        # maximum j is half of what remains
        for j in range(i, (1000 - i) / 2):
            # k is difference
            k = 1000 - i - j
            if i * i + j * j == k * k:
                print i * j * k
                return

main()
