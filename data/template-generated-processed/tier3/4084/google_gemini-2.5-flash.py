from fractions import Fraction

def solve():
    """Index: 4084.
    Returns: the number of sunflowers.
    """
    # L1
    dozen_quantity = 1 # one dozen flowers
    flowers_per_dozen = 12 # WK
    total_flowers = dozen_quantity * flowers_per_dozen

    # L2
    daisies = 2 # Two of the flowers are daisies
    non_daisy_flowers = total_flowers - daisies

    # L3
    tulip_fraction_numerator = 3 # Three-fifths of the remaining flowers
    tulip_fraction_denominator = 5 # Three-fifths of the remaining flowers
    tulip_fraction = Fraction(tulip_fraction_numerator, tulip_fraction_denominator)
    tulips = non_daisy_flowers * tulip_fraction

    # L4
    sunflowers = non_daisy_flowers - tulips

    # FA
    answer = sunflowers
    return answer