from fractions import Fraction

def solve():
    """Index: 3313.
    Returns: the number of weeks of daily tea Marco gets from a box.
    """
    # L1
    total_ounces_in_box = 28 # boxes of 28 ounces
    ounces_per_cup_fraction = Fraction(1, 5) # a fifth of an ounce
    reciprocal_of_ounces_per_cup = 5 # derived from '1/5'
    total_cups_from_box = total_ounces_in_box * reciprocal_of_ounces_per_cup

    # L2
    days_per_week = 7 # 7 days a week
    weeks_of_tea = total_cups_from_box / days_per_week

    # FA
    answer = weeks_of_tea
    return answer