from fractions import Fraction

def solve():
    """Index: 5178.
    Returns: the total amount spent on apples.
    """
    # L1
    days_per_week = 7 # WK
    weeks_needed = 2 # 2 weeks
    total_days = days_per_week * weeks_needed

    # L2
    apples_per_day = 1 # Irene shares half of a small apple with her dog every day
    total_apples_needed = apples_per_day * total_days

    # L3
    apple_weight_decimal = 0.25 # 1/4 of a pound
    apple_weight_fraction_for_calc = Fraction(1, 4) # 1/4 of a pound
    total_pounds_apples = apple_weight_fraction_for_calc * total_apples_needed

    # L4
    cost_per_pound = 2.00 # $2.00 a pound
    total_cost = total_pounds_apples * cost_per_pound

    # FA
    answer = total_cost
    return answer