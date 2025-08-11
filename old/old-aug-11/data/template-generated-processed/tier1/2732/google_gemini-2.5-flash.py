def solve():
    """Index: 2732.
    Returns: the total number of loaves of bread the baker bakes in 3 weeks.
    """
    # L1
    loaves_per_hour_per_oven = 5 # bakes 5 loaves of bread an hour in one oven
    num_ovens = 4 # He has 4 ovens
    loaves_per_hour_total = loaves_per_hour_per_oven * num_ovens

    # L2
    baking_hours_weekday = 5 # bakes for 5 hours
    loaves_per_day_weekday = baking_hours_weekday * loaves_per_hour_total

    # L3
    weekdays_in_week = 5 # WK
    total_loaves_weekday = loaves_per_day_weekday * weekdays_in_week

    # L4
    baking_hours_weekend = 2 # only bakes for 2 hours
    loaves_per_day_weekend = baking_hours_weekend * loaves_per_hour_total

    # L5
    weekend_days_in_week = 2 # WK
    total_loaves_weekend = loaves_per_day_weekend * weekend_days_in_week

    # L6
    total_loaves_per_week = total_loaves_weekday + total_loaves_weekend

    # L7
    num_weeks = 3 # in 3 weeks
    total_loaves_three_weeks = total_loaves_per_week * num_weeks

    # FA
    answer = total_loaves_three_weeks
    return answer