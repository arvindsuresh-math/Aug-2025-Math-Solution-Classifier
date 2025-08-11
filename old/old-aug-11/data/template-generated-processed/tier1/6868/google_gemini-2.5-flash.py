def solve():
    """Index: 6868.
    Returns: the total time Tim spends reading per week.
    """
    # L1
    reading_multiplier = 2 # twice as much time reading
    meditating_hours_per_day = 1 # 1 hour a day meditating
    reading_hours_per_day = reading_multiplier * meditating_hours_per_day

    # L2
    days_in_week = 7 # WK
    reading_hours_per_week = reading_hours_per_day * days_in_week

    # FA
    answer = reading_hours_per_week
    return answer