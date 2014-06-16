"""
    Problem 33:

    Problem Definition:
    The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

    We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

    There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

    If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

    Problem Solution:
    This problem can be solved easily by exploring the whole search space.
    The number of fractions with two digit numerators and denominators is less than 100 * 100.
"""
from PEUtils import PrimeFactors

# compares two floats to see if they equal eachother
# within an epsilon 1e-8
def withinEpsilon(a, b):
    if a - 1e-8 < b and a + 1e-8 > b:
        return True
    return False

# returns whether the numerator and denominator reduce in
# the way described the problem
def sillyReduce(numerator, denominator):
    reduced = float(numerator) / denominator
    # extract digits
    n_first  = numerator / 10
    n_second = numerator % 10
    d_first  = denominator / 10
    d_second = denominator % 10

    # see if they can reduce in the manner described
    if n_second == d_first \
            and withinEpsilon(float(n_first) / d_second, reduced):
                return True
    return False


def main():
    # factors in numerator and denominator
    n_factors = {}
    d_factors = {}

    # try all options, ignore multiples of 10 and 11 (they're trivial)
    for denominator in range(10, 100):
        if not denominator % 10 or not denominator % 11:
            continue

        for numerator in range(10, denominator):
            if not numerator % 10 or not numerator % 11:
                continue

            if sillyReduce(numerator, denominator):
                # add in factors
                for factor in PrimeFactors(numerator):
                    if factor in n_factors:
                        n_factors[factor] += 1
                    else:
                        n_factors[factor] = 1

                for factor in PrimeFactors(denominator):
                    if factor in d_factors:
                        d_factors[factor] += 1
                    else:
                        d_factors[factor] = 1

    # remove shared factors
    for k,v in d_factors.iteritems():
        if k in n_factors:
            d_factors[k] -= n_factors[k]
            n_factors[k] -= v

    # compute the denominator
    d_prod = 1
    for k,v in d_factors.iteritems():
        if v < 1:
            continue
        d_prod *= k ** v
    print d_prod

main()
