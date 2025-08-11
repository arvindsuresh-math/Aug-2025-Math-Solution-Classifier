from fractions import Fraction

def solve():
    """Index: 1121.
    Returns: Clara's age in 5 years.
    """
    # L1
    alice_pens = 60 # Alice has 60 pens
    clara_pens_fraction = Fraction(2, 5) # 2/5 times as many pens as Alice
    clara_pens = clara_pens_fraction * alice_pens

    # L2
    pen_difference = alice_pens - clara_pens

    # L3
    alice_age = 20 # Alice's age is 20
    clara_current_age = alice_age + pen_difference

    # L4
    years_to_add = 5 # in 5 years to come
    clara_age_in_five_years = clara_current_age + years_to_add

    # FA
    answer = clara_age_in_five_years
    return answer