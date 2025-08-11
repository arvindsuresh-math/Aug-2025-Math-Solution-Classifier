from fractions import Fraction

def solve():
    """Index: 4659.
    Returns: the number of men seated on the bus.
    """
    # L1
    total_passengers = 48 # 48 passengers on the bus
    women_fraction = Fraction(2, 3) # Two-thirds of the passengers are women
    num_women = total_passengers * women_fraction

    # L2
    num_men = total_passengers - num_women

    # L3
    standing_men_fraction = Fraction(1, 8) # one-eighth of the men are standing
    num_men_standing = num_men * standing_men_fraction

    # L4
    num_men_seated = num_men - num_men_standing

    # FA
    answer = num_men_seated
    return answer