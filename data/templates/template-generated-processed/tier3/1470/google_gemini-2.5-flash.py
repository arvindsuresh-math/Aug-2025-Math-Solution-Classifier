def solve():
    """Index: 1470.
    Returns: the total number of hours Ayen jogged this week.
    """
    # L1
    daily_jog_minutes = 30 # jogs for 30 minutes every day
    regular_weekday_count = 3 # Monday, Wednesday, and Thursday
    regular_weekday_jog_minutes = daily_jog_minutes * regular_weekday_count

    # L2
    tuesday_extra_minutes = 5 # jogged 5 minutes more
    tuesday_jog_minutes = daily_jog_minutes + tuesday_extra_minutes

    # L3
    friday_extra_minutes = 25 # jogged 25 minutes more on Friday
    friday_jog_minutes = daily_jog_minutes + friday_extra_minutes

    # L4
    total_minutes_this_week = regular_weekday_jog_minutes + tuesday_jog_minutes + friday_jog_minutes

    # L5
    minutes_per_hour = 60 # WK
    total_hours_this_week = total_minutes_this_week / minutes_per_hour

    # FA
    answer = total_hours_this_week
    return answer