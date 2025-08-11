def solve():
    """Index: 4578.
    Returns: the total number of weeks it will take Grace to get the target amount of money.
    """
    # L1
    charge_per_week = 300 # charges 300 dollars
    payment_interval_weeks = 2 # every 2 weeks
    dollars_per_interval = charge_per_week * payment_interval_weeks

    # L2
    target_amount = 1800 # get 1800 dollars
    num_intervals = target_amount / dollars_per_interval

    # L3
    total_weeks = num_intervals * payment_interval_weeks

    # FA
    answer = total_weeks
    return answer