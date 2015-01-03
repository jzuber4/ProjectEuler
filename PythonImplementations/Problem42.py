"""
    Problem 42:

    Problem Description:

    The nth term of the sequence of triangle numbers is given by,
    t_n = n * (n+1) / 2; so the first ten triangle numbers are:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    By converting each letter in a word to a number corresponding to its
    alphabetical position and adding these values we form a word value.
    For example, the word value for SKY is 19 + 11 + 25 = 55 = t_10.
    If the word value is a triangle number then we shall call the word a
    triangle word.

    Using words.txt (right click and 'Save Link/Target As...'), a 16K
    text file containing nearly two-thousand common English words, how
    many are triangle words?

    Problem Solution:
    Got the maximum possible triangle number by finding the word with
    the highest number. Then iterated over words and counted how many
    had numbers in the set of triangle numbers (calculated up to given
    highest number).

"""
from itertools import takewhile, imap, count

# turn word into numbers based on index
def numerify(word):
    return sum(ord(c) - ord('A') + 1 for c in word)

def main():
    # read all words from file
    f = open("Problem42.txt")
    words = []
    for l in f:
        for w in l.split(","):
            words.append(w[1:-1])

    # highest value of word, compute triangle numbers up to here
    top_val = max(numerify(word) for word in words)

    # get all triangle nums lte that number
    triangle_nums = set(takewhile(lambda x: x <= top_val,
                        imap(lambda x: x * (x + 1) / 2, count(1))))

    # count words that sum to triangle numbers
    print sum(1 for w in words if numerify(w) in triangle_nums)

main()
