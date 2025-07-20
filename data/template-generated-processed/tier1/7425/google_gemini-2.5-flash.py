def solve():
    """Index: 7425.
    Returns: the total number of breads Lars bakes in a day.
    """
    # L1
    loaves_per_hour = 10 # 10 loaves of bread within an hour
    baking_hours_per_day = 6 # bakes 6 hours a day
    loaves_per_day = loaves_per_hour * baking_hours_per_day

    # L2
    baguettes_per_two_hours = 30 # 30 baguettes every 2 hours
    two_hour_period = 2 # every 2 hours
    num_two_hour_periods = baking_hours_per_day / two_hour_period
    baguettes_per_day = baguettes_per_two_hours * num_two_hour_periods

    # L3
    total_breads = loaves_per_day + baguettes_per_day

    # FA
    answer = total_breads
    return answer