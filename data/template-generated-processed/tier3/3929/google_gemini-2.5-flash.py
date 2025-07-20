from fractions import Fraction

def solve():
    """Index: 3929.
    Returns: the number of egg rolls Matthew ate.
    """
    # L1
    alvin_eats = 4 # If Alvin ate 4 egg rolls
    patrick_fraction = Fraction(1, 2) # Patrick eats half as many egg rolls
    patrick_eats = patrick_fraction * alvin_eats

    # L2
    matthew_multiplier = 3 # Matthew eats three times as many egg rolls
    matthew_eats = matthew_multiplier * patrick_eats

    # FA
    answer = matthew_eats
    return answer