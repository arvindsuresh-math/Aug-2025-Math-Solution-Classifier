def solve():
    """Index: 7012.
    Returns: the total amount Jake earns in 5 days.
    """
    # L1
    jacob_hourly_wage = 6 # Jacob earns $6 per hour
    jake_multiplier = 3 # Jake earns thrice what Jacob does
    jake_hourly_wage = jacob_hourly_wage * jake_multiplier

    # L2
    hours_per_day = 8 # working 8 hours a day
    jake_daily_earnings = jake_hourly_wage * hours_per_day

    # L3
    num_days = 5 # in 5 days
    jake_total_earnings = jake_daily_earnings * num_days

    # FA
    answer = jake_total_earnings
    return answer