"""
    Problem 31:

    Problem Description:
    In England the currency is made up of pounds and pence, p, and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, 1 pound (100p) and 2 pound (200p).
    It is possible to make 2 pounds in the following way:

    1*100p + 1*50p + 2*20p + 1*5p + 1*2p + 3*1p
    How many different ways can 2 pounds be made using any number of coins?

    Problem Solution:
        Greedily take from the total with the largest coin, then recurse into sub problems eliminating
        the largest coin.
"""
from PEUtils import OptionalArg

def waysToTake(pence, coins):
    if len(coins) == 1 or pence == 0:
        return 1

    # for each choice of number of coins, recurse
    largest_coin = coins[0]
    return sum(waysToTake(pence - i * largest_coin, coins[1:])
                          for i in range(pence / largest_coin + 1))


def main():
    N = int(OptionalArg(0, 200))

    print waysToTake(N, [200, 100, 50, 20, 10, 5, 2, 1])

main()
