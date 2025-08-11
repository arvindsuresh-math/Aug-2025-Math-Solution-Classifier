from fractions import Fraction

def solve():
    """Index: 6446.
    Returns: the number of bottles of water remaining after 2 days.
    """
    # L1
    total_bottles = 24 # a 24 pack of bottled water
    fraction_day1 = Fraction(1, 3) # 1/3 of them on the first day
    drank_day1 = total_bottles * fraction_day1

    # L2
    remaining_after_day1 = total_bottles - drank_day1

    # L3
    fraction_day2 = Fraction(1, 2) # 1/2 of what was left after the first day on the second day
    drank_day2 = remaining_after_day1 * fraction_day2

    # FA
    answer = drank_day2
    return answer