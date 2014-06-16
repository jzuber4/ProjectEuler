"""
Problem 26: Reciprocal cycles
Returns the number d < N where 1 / d has the longest recurring cycle
N defaults to 1000
usage:
$ python Problem26.py [N = 1000]
"""

from PEUtils import OptionalArg

# perform one step of long division
def LongDivisionStep(dividend, divisor):
    index = 1
    dividend_string = str(dividend)
    dividend_term = int(dividend_string[:index])
    quotient = ""
    first = True

    # increase size of divided part until it is greater than the divisor
    while divisor > dividend_term:
        index += 1
        if len(dividend_string) < index:
            dividend_string += "0"
            quotient += "0"

        dividend_term = int(dividend_string[:index])

    # perform the division
    quotient += str(dividend_term / divisor)
    remainder = dividend_term - divisor * (dividend_term / divisor)
    new_dividend = int(str(remainder) + dividend_string[index:])
    return quotient, new_dividend

def LongDivision(dividend, divisor):
    seen_dividends = set()
    quotient_string = ""

    while dividend != 0:
        # performs a step of long division, and returns the quotient and dividend
        quotient, dividend = LongDivisionStep(dividend, divisor)
        quotient_string += quotient

        # repeating digits detection
        if dividend in seen_dividends:
            return quotient_string

        # we have seen this
        seen_dividends.add(dividend)

        # advance to the next iteration
        dividend *= 10

    return quotient_string

def main():
    N = int(OptionalArg(0, 1000))
    max_v = 1
    max_len = 0
    for i in range(1, N + 1):
        s = LongDivision(1, i)
        if len(s) > max_len:
            max_len = len(s)
            max_v = i

    print max_v

main()
