def solve():
    """Index: 2055.
    Returns: how much Sarah makes in an 8-hour day.
    """
    # L1
    connor_hourly = 7.2 # Connor earns $7.20 per hour
    sarah_multiplier = 5 # Sarah makes 5 times more money per hour
    sarah_hourly = connor_hourly * sarah_multiplier

    # L2
    workday_hours = 8 # 8-hour day
    sarah_daily = sarah_hourly * workday_hours

    # FA
    answer = sarah_daily
    return answer