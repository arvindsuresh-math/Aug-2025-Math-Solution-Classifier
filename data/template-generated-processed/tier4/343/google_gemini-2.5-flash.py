def solve():
    """Index: 343.
    Returns: the cost in cents to run the TV for a week.
    """
    # L1
    hours_per_day = 4 # 4 hours a day
    watts_per_hour = 125 # 125 watts of electricity per hour
    watt_hours_per_day = hours_per_day * watts_per_hour

    # L2
    days_per_week = 7 # WK
    watt_hours_per_week = watt_hours_per_day * days_per_week

    # L3
    watts_per_kw = 1000 # WK
    kwh_per_week = watt_hours_per_week / watts_per_kw

    # L4
    cost_per_kwh_dollars = 0.14 # 14 cents per kw/h (used as $0.14 in solution)
    cost_per_week_dollars = kwh_per_week * cost_per_kwh_dollars

    # Convert to cents as requested by the question
    cents_per_dollar = 100 # WK
    cost_per_week_cents = cost_per_week_dollars * cents_per_dollar

    # FA
    answer = cost_per_week_cents
    return answer