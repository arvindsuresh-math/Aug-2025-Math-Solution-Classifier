from fractions import Fraction

def solve():
    """Index: 7349.
    Returns: the total number of cups of sugar used.
    """
    # L1
    sugar_ratio_part = 1 # ratio of 1:2
    water_ratio_part = 2 # ratio of 1:2
    total_ratio_parts = sugar_ratio_part + water_ratio_part

    # L2
    sugar_numerator = 1 # ratio of 1:2
    sugar_denominator = total_ratio_parts
    sugar_fraction = Fraction(sugar_numerator, sugar_denominator)

    # L3
    total_cups_used = 84 # she used 84 cups
    sugar_cups_used = sugar_fraction * total_cups_used

    # FA
    answer = sugar_cups_used
    return answer