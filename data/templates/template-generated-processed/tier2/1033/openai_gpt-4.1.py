def solve():
    """Index: 1033.
    Returns: the number of calories James loses a week from dancing.
    """
    # L1
    walking_calories_per_hour = 300 # burned 300 calories an hour walking
    dance_calories_multiplier = 2 # loses twice as many calories per hour as he did when he was walking
    dance_calories_per_hour = dance_calories_multiplier * walking_calories_per_hour

    # L2
    dance_session_duration = 0.5 # .5 hours each time
    dance_sessions_per_day = 2 # dances twice a day
    dance_hours_per_day = dance_session_duration * dance_sessions_per_day

    # L3
    calories_per_day = dance_calories_per_hour * dance_hours_per_day

    # L4
    dance_days_per_week = 4 # does this 4 times a week
    calories_per_week = calories_per_day * dance_days_per_week

    # FA
    answer = calories_per_week
    return answer