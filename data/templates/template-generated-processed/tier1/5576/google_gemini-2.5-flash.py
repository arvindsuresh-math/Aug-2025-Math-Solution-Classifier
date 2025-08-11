def solve():
    """Index: 5576.
    Returns: the total amount Mitch earns every week.
    """
    # L1
    hours_weekday = 5 # works 5 hours every day from Monday to Friday
    hourly_rate_weekday = 3 # earns $3 per hour
    earnings_per_weekday = hours_weekday * hourly_rate_weekday

    # L2
    num_weekdays = 5 # Monday to Friday
    total_earnings_weekdays = earnings_per_weekday * num_weekdays

    # L3
    weekend_multiplier = 2 # earns double on weekends
    hourly_rate_weekend = hourly_rate_weekday * weekend_multiplier

    # L4
    hours_weekend_day = 3 # 3 hours every Saturday and Sunday
    earnings_per_weekend_day = hourly_rate_weekend * hours_weekend_day

    # L5
    num_weekend_days = 2 # every Saturday and Sunday
    total_earnings_weekend = earnings_per_weekend_day * num_weekend_days

    # L6
    total_weekly_earnings = total_earnings_weekdays + total_earnings_weekend

    # FA
    answer = total_weekly_earnings
    return answer