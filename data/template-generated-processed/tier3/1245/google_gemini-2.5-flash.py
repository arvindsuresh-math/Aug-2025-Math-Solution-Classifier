from fractions import Fraction

def solve():
    """Index: 1245.
    Returns: the number of watermelons left to be sold tomorrow.
    """
    # L1
    initial_dozens = 10 # 10 dozens of watermelons
    items_per_dozen = 12 # WK
    total_watermelons = initial_dozens * items_per_dozen

    # L2
    yesterday_percentage = Fraction(40, 100) # sold 40% of it yesterday
    sold_yesterday = total_watermelons * yesterday_percentage

    # L3
    remaining_after_yesterday = total_watermelons - sold_yesterday

    # L4
    today_fraction = Fraction(1, 4) # 1/4 of the remaining today
    sold_today = remaining_after_yesterday * today_fraction

    # L5
    left_for_tomorrow = remaining_after_yesterday - sold_today

    # FA
    answer = left_for_tomorrow
    return answer