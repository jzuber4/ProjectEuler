"""
Problem 26: Reciprocal cycles
Returns the number d < N where 1 / d has the longest recurring cycle
N defaults to 1000
usage:
$ python Problem26.py [N = 1000]
"""

from PEUtils import OptionalArg
def LongDivisionStep(dividend, divisor):
    index = 1
    dividend_string = str(dividend)
    dividend_term = int(dividend_string[:1])
    quotient = ""
    first = True
    while divisor > dividend_term:
        index += 1
        if len(dividend_string) < index:
            dividend_string += "0"
            quotient += "0"

        dividend_term = int(dividend_string[:index])

    quotient += str(dividend_term / divisor)
    remainder = dividend_term - divisor * (dividend_term / divisor)
    new_dividend = int(str(remainder) + dividend_string[index:])
    return quotient, new_dividend

def LongDivision(dividend, divisor):
    quotients = []
    seen_dividends = {}
    index = 0
    has_decimal = False
    digits_until_decimal = len(str(dividend))
    digits_remaining = digits_until_decimal
    while dividend != 0:
        quotient, dividend = LongDivisionStep(dividend, divisor)
        digits_remaining -= len(str(quotient))

        # repeating digits detection
        if dividend in seen_dividends:
            formatted = ""
            seen_index = seen_dividends[dividend]
            for i, q in enumerate(quotients):
                if i == seen_index:
                    formatted += "("
                formatted += q
            formatted += ")"
            return formatted[:digits_until_decimal] + "." + formatted[digits_until_decimal:]

        # save last time that dividend has been seen
        if digits_remaining < 0:
            seen_dividends[dividend] = index

        quotients.append(quotient)

        # advance to the next iteration
        index += 1
        dividend *= 10

    formatted = reduce(lambda built_string, quotient: built_string + quotient, quotients)
    return formatted[:digits_until_decimal] + "." + formatted[digits_until_decimal:]

def main():
    N = OptionalArg(0, 1000)
    print LongDivision(1, 3)

main()
