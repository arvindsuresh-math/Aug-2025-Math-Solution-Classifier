def solve():
    """Index: 264.
    Returns: the total money the restaurant earns by the end of the month.
    """
    # L1
    weekday_earning = 600 # earns $600 every weekday
    weekdays_per_week = 5 # 5 weekdays
    weekday_total = weekday_earning * weekdays_per_week

    # L2
    weekend_multiplier = 2 # twice as much on the weekend
    weekend_days_per_week = 2 # 2 weekend days
    weekend_total = (weekday_earning * weekend_multiplier) * weekend_days_per_week

    # L3
    weekly_total = weekday_total + weekend_total

    # L4
    weeks_per_month = 4 # 4 weeks
    monthly_total = weekly_total * weeks_per_month

    # FA
    answer = monthly_total
    return answer