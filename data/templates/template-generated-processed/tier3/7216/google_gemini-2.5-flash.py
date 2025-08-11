from fractions import Fraction

def solve():
    """Index: 7216.
    Returns: the difference in height between James's uncle and James.
    """
    # L1
    uncle_height = 72 # uncle who is 72 inches
    james_initial_height_fraction = Fraction(2, 3) # 2/3s as tall
    james_initial_height = uncle_height * james_initial_height_fraction

    # L2
    growth_spurt_gain = 10 # gain 10 inches
    james_current_height = james_initial_height + growth_spurt_gain

    # L3
    height_difference = uncle_height - james_current_height

    # FA
    answer = height_difference
    return answer