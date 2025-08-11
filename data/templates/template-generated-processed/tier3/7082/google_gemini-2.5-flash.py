from fractions import Fraction

def solve():
    """Index: 7082.
    Returns: the number of pizza slices left for tomorrow's lunch.
    """
    # L1
    total_slices = 12 # Donna cut her pizza into 12 slices
    lunch_divisor = 2 # ate half for lunch
    slices_after_lunch = total_slices / lunch_divisor

    # L2
    dinner_fraction = Fraction(1, 3) # ate 1/3 of the remaining pizza for dinner
    dinner_slices = dinner_fraction * slices_after_lunch

    # L3
    slices_for_tomorrow = slices_after_lunch - dinner_slices

    # FA
    answer = slices_for_tomorrow
    return answer