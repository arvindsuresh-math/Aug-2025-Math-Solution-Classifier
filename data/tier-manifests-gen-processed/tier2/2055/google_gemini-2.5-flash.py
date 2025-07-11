def solve():
    """Index: 2055.
    Returns: how much Sarah makes in an 8-hour day.
    """
    # L1
    connor_hourly_wage = 7.2 # Connor earns $7.20 per hour
    sarah_wage_multiplier = 5 # Sarah makes 5 times more money per hour than Connor does
    sarah_hourly_wage = connor_hourly_wage * sarah_wage_multiplier

    # L2
    daily_hours = 8 # an 8-hour day
    sarah_daily_wage = sarah_hourly_wage * daily_hours

    # FA
    answer = sarah_daily_wage
    return answer