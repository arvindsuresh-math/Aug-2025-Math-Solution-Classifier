def solve():
    """Index: 4780.
    Returns: the total amount Arman will receive for working two weeks.
    """
    # L1
    last_week_hours = 35 # 35 hours
    hourly_rate_last_week = 10 # $10 per hour
    earnings_last_week = last_week_hours * hourly_rate_last_week

    # L2
    this_week_hours = 40 # 40 hours
    hourly_rate_increase = 0.5 # increase of $0.5 per hour
    hourly_rate_this_week = hourly_rate_last_week + hourly_rate_increase
    earnings_this_week = this_week_hours * hourly_rate_this_week

    # L3
    total_earnings = earnings_last_week + earnings_this_week

    # FA
    answer = total_earnings
    return answer