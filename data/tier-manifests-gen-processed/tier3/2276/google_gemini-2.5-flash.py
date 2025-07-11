from fractions import Fraction

def solve():
    """Index: 2276.
    Returns: the final volume of the syrup in cups.
    """
    # L1
    initial_quarts = 6 # 6 quarts of juice
    cups_per_quart = 4 # 4 cups in a quart
    initial_cups = initial_quarts * cups_per_quart

    # L2
    reduction_fraction = Fraction(1, 12) # 1/12 of its original volume
    reduced_volume_cups = initial_cups * reduction_fraction

    # L3
    sugar_volume_cups = 1 # adds 1 cup of sugar
    final_volume_syrup = reduced_volume_cups + sugar_volume_cups

    # FA
    answer = final_volume_syrup
    return answer