def solve():
    """Index: 3288.
    Returns: the total hours of TV Flynn watches in 52 weeks.
    """
    # L1
    minutes_per_night = 30 # 30 minutes of tv every night
    weekdays_per_week = 5 # weekdays
    weekday_minutes_per_week = minutes_per_night * weekdays_per_week

    # L2
    weekend_hours = 2 # additional 2 hours of TV
    minutes_per_hour = 60 # WK
    weekend_minutes_per_week = weekend_hours * minutes_per_hour

    # L3
    total_minutes_per_week = weekday_minutes_per_week + weekend_minutes_per_week

    # L4
    total_weeks = 52 # in 52 weeks
    total_minutes_per_year = total_weeks * total_minutes_per_week

    # L5
    total_hours_per_year = total_minutes_per_year / minutes_per_hour

    # FA
    answer = total_hours_per_year
    return answer