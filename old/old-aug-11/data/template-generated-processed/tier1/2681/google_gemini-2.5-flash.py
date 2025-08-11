def solve():
    """Index: 2681.
    Returns: Jonathan's weekly caloric deficit.
    """
    # L1
    calories_daily_normal = 2500 # Jonathan eats 2500 calories every day
    extra_calories_saturday = 1000 # consumes an extra 1000 calories
    calories_saturday = calories_daily_normal + extra_calories_saturday

    # L2
    days_in_week = 7 # WK
    days_not_saturday = days_in_week - 1 # every day except for Saturday
    total_calories_consumed_weekly = calories_daily_normal * days_not_saturday + calories_saturday

    # L3
    calories_burned_daily = 3000 # He burns 3000 calories every day
    total_calories_burned_weekly = calories_burned_daily * days_in_week

    # L4
    caloric_deficit_weekly = total_calories_burned_weekly - total_calories_consumed_weekly

    # FA
    answer = caloric_deficit_weekly
    return answer