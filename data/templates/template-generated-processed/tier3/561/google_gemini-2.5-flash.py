from fractions import Fraction

def solve():
    """Index: 561.
    Returns: the age of the granddaughter.
    """
    # L1
    daughter_younger_percentage = Fraction(40, 100) # 40 percent younger than she is
    betty_age = 60 # Betty is 60 years old
    daughter_age_reduction = daughter_younger_percentage * betty_age

    # L2
    daughter_age = betty_age - daughter_age_reduction

    # L3
    granddaughter_age_fraction = Fraction(1, 3) # one-third her mother's age
    granddaughter_age = granddaughter_age_fraction * daughter_age

    # FA
    answer = granddaughter_age
    return answer