"""
Problem 17: Number letter counts
Prints the number of letters used to spell out the numbers from 1 to N inclusive
N defaults to 1000
usage:
python Problem17.py [N = 1000]
"""
import sys

one_to_ten = [len(i) for i in ["one", "two", "three", "four", "five",
                               "six", "seven", "eight", "nine"]]
ten_to_twenty = [len(i) for i in ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
                                  "sixteen", "seventeen", "eighteen", "nineteen"]]
twenty_to_one_hundred = [len(i) for i in ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
                                          "eighty", "ninety"]]

# recursive function for calculating number of letters
def NumberOfLetters(n):
    if n == 0:
        return 0
    elif n < 10:
        return one_to_ten[n-1]
    elif n < 20:
        return ten_to_twenty[n - 10]
    elif n < 100:
        return twenty_to_one_hundred[(n / 10) - 2] + NumberOfLetters(n % 10)
    elif n < 1000 and n % 100 == 0:
        return NumberOfLetters(n / 100) + len("hundred")
    elif n < 1000:
        return NumberOfLetters(n / 100) + len("hundredand") + NumberOfLetters(n % 100)
    elif n < 1000000:
        return NumberOfLetters(n / 1000) + len("thousand") + NumberOfLetters(n % 1000)

def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 1000

    print sum(NumberOfLetters(i) for i in range(1, N+1))

main()
