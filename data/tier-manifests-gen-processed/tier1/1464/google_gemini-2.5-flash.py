def solve():
    """Index: 1464.
    Returns: the total toilet paper production during March of 2020.
    """
    # L1
    initial_daily_production = 7000 # producing 7000 toilet paper per day
    increase_multiplier = 3 # three times more
    increased_amount_per_day = increase_multiplier * initial_daily_production

    # L2
    total_daily_production = initial_daily_production + increased_amount_per_day

    # L3
    days_in_march = 31 # In March, with 31 days
    total_production_march = total_daily_production * days_in_march

    # FA
    answer = total_production_march
    return answer