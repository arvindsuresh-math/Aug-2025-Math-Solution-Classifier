def solve():
    """Index: 264.
    Returns: the total money earned by the end of the month.
    """
    # L1
    weekday_earnings_per_day = 600 # earns $600 every weekday
    num_weekdays_per_week = 5 # WK
    total_weekday_earnings_per_week = weekday_earnings_per_day * num_weekdays_per_week

    # L2
    multiplier_weekend = 2 # twice as much on the weekend
    num_weekend_days_per_week = 2 # WK
    total_weekend_earnings_per_week = (weekday_earnings_per_day * multiplier_weekend) * num_weekend_days_per_week

    # L3
    total_weekly_earnings = total_weekday_earnings_per_week + total_weekend_earnings_per_week

    # L4
    num_weeks_per_month = 4 # WK
    total_monthly_earnings = total_weekly_earnings * num_weeks_per_month

    # FA
    answer = total_monthly_earnings
    return answer