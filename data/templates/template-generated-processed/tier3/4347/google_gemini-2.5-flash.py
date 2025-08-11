from fractions import Fraction

def solve():
    """Index: 4347.
    Returns: the total number of cutlery pieces Braelynn has in her kitchen.
    """
    # L1
    initial_knives = 24 # 24 knives
    additional_knives_fraction = Fraction(1, 3) # 1/3 as many additional knives
    additional_knives = additional_knives_fraction * initial_knives

    # L2
    total_knives = initial_knives + additional_knives

    # L3
    teaspoons_multiplier = 2 # twice as many teaspoons as knives
    initial_teaspoons = teaspoons_multiplier * initial_knives

    # L4
    additional_teaspoons_fraction = Fraction(2, 3) # 2/3 as many additional teaspoons
    additional_teaspoons = additional_teaspoons_fraction * initial_teaspoons

    # L5
    total_teaspoons = additional_teaspoons + initial_teaspoons

    # L6
    total_cutlery = total_teaspoons + total_knives

    # FA
    answer = total_cutlery
    return answer