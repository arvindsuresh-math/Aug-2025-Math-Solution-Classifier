def solve():
    """Index: 2732.
    Returns: the number of loaves of bread the baker bakes in 3 weeks.
    """
    # L1
    loaves_per_hour = 5 # bakes 5 loaves of bread an hour
    ovens = 4 # he has 4 ovens
    loaves_per_hour_total = loaves_per_hour * ovens

    # L2
    weekday_hours = 5 # bakes for 5 hours (Mon-Fri)
    weekday_loaves_per_day = weekday_hours * loaves_per_hour_total

    # L3
    weekdays = 5 # Monday to Friday
    weekday_loaves_total = weekday_loaves_per_day * weekdays

    # L4
    weekend_hours = 2 # bakes for 2 hours (Sat/Sun)
    weekend_loaves_per_day = weekend_hours * loaves_per_hour_total

    # L5
    weekend_days = 2 # Saturday and Sunday
    weekend_loaves_total = weekend_loaves_per_day * weekend_days

    # L6
    loaves_per_week = weekday_loaves_total + weekend_loaves_total

    # L7
    weeks = 3 # in 3 weeks
    total_loaves = loaves_per_week * weeks

    # FA
    answer = total_loaves
    return answer