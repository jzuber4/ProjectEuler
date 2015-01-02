"""
    Problem 38:

    Problem Description:


    Take the number 192 and multiply it by each of 1, 2, and 3:

    192 * 1 = 192
    192 * 2 = 384
    192 * 3 = 576

    By concatenating each product we get the 1 to 9 pandigital, 192384576.
    We will call 192384576 the concatenated product of 192 and (1,2,3)

    The same can be achieved by starting with 9 and multiplying by
    1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the
    concatenated product of 9 and (1,2,3,4,5).

    What is the largest 1 to 9 pandigital 9-digit number that can be
    formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

    Problem Solution:
    Starting with k=9, try each (1, 2, .., n) * k concatenated product until n = 10000
    (10,000 chosen by experimentation) then print maximum found pandigital.
"""
# add each nonzero digit to a set
# if there are 9 digits in the set, it is a 1 to 9 pandigital
def is_pandigital(num_string):
    digits = set()
    for c in num_string:
        if c != '0':
            digits.add(c)
    return len(digits) == 9

def main():
    best = 0
    for k in range(9, 10000):
        concatenated_product = ""
        for i in range(1, 10):
            concatenated_product += str(i * k)
            if len(concatenated_product) > 9:
                # too long for 1 to 9 pandigital
                break
            elif len(concatenated_product) == 9:
                # candidate for 1 to 9 pandigital
                if is_pandigital(concatenated_product):
                    num = int(concatenated_product)
                    if num > best:
                        best = num
                break
    print best

main()
