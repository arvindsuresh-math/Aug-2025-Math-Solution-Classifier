def solve():
    """Index: 2570.
    Returns: Kenneth's total earnings for the week.
    """
    # L1
    spent_percent = 10 # Kenneth spent 10%
    total_percent = 100 # WK
    left_percent = total_percent - spent_percent

    # L2
    left_amount = 405 # he is left with $405
    one_percent_value = left_amount / left_percent

    # L3
    earnings = one_percent_value * total_percent

    # FA
    answer = earnings
    return answer