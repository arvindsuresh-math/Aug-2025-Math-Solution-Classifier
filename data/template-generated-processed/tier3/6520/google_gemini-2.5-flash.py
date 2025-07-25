def solve():
    """Index: 6520.
    Returns: the number of weeks it takes for Doris to earn enough to cover her monthly expenses.
    """
    # L1
    weekdays_per_week = 5 # WK
    hours_per_weekday = 3 # 3 hours every weekday
    weekday_hours = weekdays_per_week * hours_per_weekday

    # L2
    saturday_hours = 5 # 5 hours on a Saturday
    total_weekly_hours = weekday_hours + saturday_hours

    # L3
    weekly_hours_for_earnings = 24 # Value used in solution's calculation
    hourly_rate = 20 # $20 per hour
    weekly_earnings = weekly_hours_for_earnings * hourly_rate

    # L4
    target_earnings = 1440 # Value used in solution's calculation
    weeks_needed = target_earnings / weekly_earnings

    # FA
    answer = weeks_needed
    return answer