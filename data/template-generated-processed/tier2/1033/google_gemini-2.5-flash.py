def solve():
    """Index: 1033.
    Returns: the total calories lost per week from dancing.
    """
    # L1
    dancing_multiplier = 2 # loses twice as many calories
    walking_calories_per_hour = 300 # burned 300 calories an hour walking
    dancing_calories_per_hour = dancing_multiplier * walking_calories_per_hour

    # L2
    daily_dance_duration_per_session = 0.5 # for .5 hours each time
    daily_dance_sessions = 2 # dances twice a day
    total_daily_dance_hours = daily_dance_duration_per_session * daily_dance_sessions

    # L3
    calories_per_day = dancing_calories_per_hour * total_daily_dance_hours

    # L4
    dance_days_per_week = 4 # 4 times a week
    calories_per_week = calories_per_day * dance_days_per_week

    # FA
    answer = calories_per_week
    return answer