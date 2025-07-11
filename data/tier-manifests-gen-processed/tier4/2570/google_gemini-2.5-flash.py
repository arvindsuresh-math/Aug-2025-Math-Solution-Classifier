def solve():
    """Index: 2570.
    Returns: Kenneth's total earnings.
    """
    # L1
    spent_percent = 10 # spent 10% of this earnings
    total_percent = 100 # WK
    remaining_percent = total_percent - spent_percent

    # L2
    remaining_amount = 405 # left with $405
    one_percent_value = remaining_amount / remaining_percent

    # L3
    percent_multiplier = 100 # WK
    total_earnings = one_percent_value * percent_multiplier

    # FA
    answer = total_earnings
    return answer