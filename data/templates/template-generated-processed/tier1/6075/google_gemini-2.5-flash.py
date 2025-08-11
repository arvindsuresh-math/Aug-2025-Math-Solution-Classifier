def solve():
    """Index: 6075.
    Returns: the total amount Tim pays the bodyguards in a week.
    """
    # L1
    bodyguard_hourly_rate = 20 # $20 an hour
    num_bodyguards = 2 # two bodyguards
    cost_per_hour_both = bodyguard_hourly_rate * num_bodyguards

    # L2
    hours_per_day = 8 # 8 hour per day
    cost_per_day = cost_per_hour_both * hours_per_day

    # L3
    days_per_week = 7 # 7 days a week
    cost_per_week = cost_per_day * days_per_week

    # FA
    answer = cost_per_week
    return answer