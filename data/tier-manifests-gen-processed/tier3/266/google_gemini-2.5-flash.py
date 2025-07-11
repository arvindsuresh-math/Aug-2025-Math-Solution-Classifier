def solve():
    """Index: 266.
    Returns: the total hours John spends at the gym a week.
    """
    # L1
    weightlifting_minutes_per_hour = 60 # 1 hour each day lifting weight
    warmup_fraction_denominator = 3 # a third of his weightlifting time
    warmup_minutes = weightlifting_minutes_per_hour / warmup_fraction_denominator

    # L2
    weightlifting_minutes_per_day = 60 # 1 hour each day lifting weight
    total_minutes_per_day = weightlifting_minutes_per_day + warmup_minutes

    # L3
    gym_days_per_week = 3 # 3 times a week
    total_minutes_per_week = total_minutes_per_day * gym_days_per_week

    # L4
    minutes_per_hour = 60 # WK
    total_hours_per_week = total_minutes_per_week / minutes_per_hour

    # FA
    answer = total_hours_per_week
    return answer