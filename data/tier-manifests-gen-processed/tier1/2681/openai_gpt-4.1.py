def solve():
    """Index: 2681.
    Returns: Jonathan's weekly caloric deficit.
    """
    # L1
    calories_per_day = 2500 # eats 2500 calories every day
    extra_calories_saturday = 1000 # extra 1000 calories on Saturday
    saturday_calories = calories_per_day + extra_calories_saturday

    # L2
    non_saturday_days = 6 # every day except for Saturday
    total_weekly_calories = calories_per_day * non_saturday_days + saturday_calories

    # L3
    calories_burned_per_day = 3000 # burns 3000 calories every day
    days_in_week = 7 # WK
    total_weekly_burned = calories_burned_per_day * days_in_week

    # L4
    caloric_deficit = total_weekly_burned - total_weekly_calories

    # FA
    answer = caloric_deficit
    return answer