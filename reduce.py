from fractions import Fraction
from functools import reduce

# fracs = [ [1, 2], [3, 4], [10, 6] ]
def product(fracs):
    t =   reduce(lambda x, y : x * y, fracs)
    return t.numerator, t.denominator