from fractions import Fraction

def solve():
    """Index: 2234.
    Returns: the amount of money left from Susie's earnings last week.
    """
    # L1
    rate_per_hour = 10 # $10 per hour
    hours_per_day = 3 # 3 hours a day
    earnings_per_day = rate_per_hour * hours_per_day

    # L2
    days_in_a_week = 7 # last week
    total_earnings_last_week = earnings_per_day * days_in_a_week

    # L3
    makeup_fraction = Fraction(3, 10) # 3/10 of the money
    spent_on_makeup = total_earnings_last_week * makeup_fraction

    # L4
    skincare_fraction = Fraction(2, 5) # 2/5 of her money
    spent_on_skincare = total_earnings_last_week * skincare_fraction

    # L5
    total_spent = spent_on_makeup + spent_on_skincare

    # L6
    money_left = total_earnings_last_week - total_spent

    # FA
    answer = money_left
    return answer