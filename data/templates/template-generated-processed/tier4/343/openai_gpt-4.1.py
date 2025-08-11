def solve():
    """Index: 343.
    Returns: the cost in cents to run Kim's TV for a week.
    """
    # L1
    hours_per_day = 4 # She runs it for 4 hours a day
    watts_per_hour = 125 # TV uses 125 watts of electricity per hour
    watt_hours_per_day = hours_per_day * watts_per_hour

    # L2
    days_per_week = 7 # WK
    watt_hours_per_week = watt_hours_per_day * days_per_week

    # L3
    watts_per_kw = 1000 # WK
    kw_hours_per_week = watt_hours_per_week / watts_per_kw

    # L4
    cost_per_kw_hour = 0.14 # electricity cost 14 cents per kw/h
    weekly_cost_dollars = kw_hours_per_week * cost_per_kw_hour

    # Convert dollars to cents
    cents_per_dollar = 100 # WK
    answer = weekly_cost_dollars * cents_per_dollar
    return answer