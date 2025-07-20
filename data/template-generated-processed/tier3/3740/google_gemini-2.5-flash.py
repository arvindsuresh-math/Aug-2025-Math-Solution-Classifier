from fractions import Fraction

def solve():
    """Index: 3740.
    Returns: Grace's age.
    """
    # L1
    grandmother_multiplier = 2 # twice the age
    mother_age = 80 # Grace's mother is 80 years old
    grandmother_age = grandmother_multiplier * mother_age

    # L2
    grace_age_fraction = Fraction(3, 8) # 3/8th the age
    grace_age = grace_age_fraction * grandmother_age

    # FA
    answer = grace_age
    return answer