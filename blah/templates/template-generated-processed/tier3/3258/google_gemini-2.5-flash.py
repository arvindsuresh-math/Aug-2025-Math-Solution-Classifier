from fractions import Fraction

def solve():
    """Index: 3258.
    Returns: the number of sausages left.
    """
    # L1
    initial_sausages = 600 # prepared 600 boar sausages
    monday_fraction = Fraction(2, 5) # ate 2/5 of them on Monday
    sausages_eaten_monday = monday_fraction * initial_sausages

    # L2
    remaining_after_monday = initial_sausages - sausages_eaten_monday

    # L3
    tuesday_divisor = 2 # half of the remaining on Tuesday
    sausages_eaten_tuesday = remaining_after_monday / tuesday_divisor

    # L4
    remaining_for_friday = remaining_after_monday - sausages_eaten_tuesday

    # L5
    friday_fraction = Fraction(3, 4) # ate 3/4 of the remaining boar sausages on Friday
    sausages_eaten_friday = friday_fraction * remaining_for_friday

    # L6
    final_remaining_sausages = remaining_for_friday - sausages_eaten_friday

    # FA
    answer = final_remaining_sausages
    return answer