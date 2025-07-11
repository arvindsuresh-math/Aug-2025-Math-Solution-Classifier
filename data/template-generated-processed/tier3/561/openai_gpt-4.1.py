from fractions import Fraction

def solve():
    """Index: 561.
    Returns: the age of the granddaughter.
    """
    # L1
    betty_age = 60 # Betty is 60 years old
    daughter_younger_fraction = Fraction(40, 100) # 40 percent younger
    daughter_younger_years = daughter_younger_fraction * betty_age

    # L2
    daughter_age = betty_age - daughter_younger_years

    # L3
    granddaughter_fraction = Fraction(1, 3) # one-third her mother's age
    granddaughter_age = granddaughter_fraction * daughter_age

    # FA
    answer = granddaughter_age
    return answer