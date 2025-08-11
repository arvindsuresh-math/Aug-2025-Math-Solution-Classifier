def solve():
    """Index: 5630.
    Returns: the amount of money Sara was left with.
    """
    # L1
    hours_per_week = 40 # worked 40 hours a week
    num_weeks = 2 # two weeks of work
    total_hours_worked = hours_per_week * num_weeks

    # L2
    hourly_rate = 11.50 # at $11.50 per hour
    total_earnings = hourly_rate * total_hours_worked

    # L3
    tire_cost = 410 # for $410
    money_left = total_earnings - tire_cost

    # FA
    answer = money_left
    return answer