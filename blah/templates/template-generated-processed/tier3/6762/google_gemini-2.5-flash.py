from fractions import Fraction

def solve():
    """Index: 6762.
    Returns: the number of cats that are spotted and fluffy.
    """
    # L1
    fraction_spotted = Fraction(1, 3) # A third of all the cats
    fraction_fluffy_of_spotted = Fraction(1, 4) # A quarter of the spotted cats
    fraction_spotted_and_fluffy = fraction_spotted * fraction_fluffy_of_spotted

    # L2
    total_cats = 120 # 120 cats in the village
    spotted_and_fluffy_cats = total_cats / fraction_spotted_and_fluffy.denominator

    # FA
    answer = spotted_and_fluffy_cats
    return answer