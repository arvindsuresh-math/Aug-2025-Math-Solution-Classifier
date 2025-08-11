from fractions import Fraction

def solve():
    """Index: 4909.
    Returns: the number of cows on the farm with no spot.
    """
    # L1
    total_cows = 140 # 140 cows
    red_spot_percentage = Fraction(40, 100) # Forty percent of the cows
    cows_with_red_spots = red_spot_percentage * total_cows

    # L2
    cows_without_red_spots = total_cows - cows_with_red_spots

    # L3
    blue_spot_percentage = Fraction(25, 100) # 25 percent of the cows
    cows_with_blue_spots = blue_spot_percentage * cows_without_red_spots

    # L4
    cows_without_any_spot = cows_without_red_spots - cows_with_blue_spots

    # FA
    answer = cows_without_any_spot
    return answer