def solve():
    """Index: 266.
    Returns: the total number of hours John spends at the gym per week.
    """
    # L1
    weightlifting_minutes = 60 # 1 hour each day lifting weight
    warmup_fraction = 3 # a third of his weightlifting time
    warmup_minutes = weightlifting_minutes / warmup_fraction

    # L2
    total_minutes_per_day = weightlifting_minutes + warmup_minutes

    # L3
    gym_days_per_week = 3 # goes to the gym 3 times a week
    total_minutes_per_week = total_minutes_per_day * gym_days_per_week

    # L4
    minutes_per_hour = 60 # WK
    total_hours_per_week = total_minutes_per_week / minutes_per_hour

    # FA
    answer = total_hours_per_week
    return answer