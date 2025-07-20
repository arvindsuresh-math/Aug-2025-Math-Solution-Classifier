def solve():
    """Index: 7403.
    Returns: the total hours James trains in a year.
    """
    # L1
    hours_per_session = 4 # 4 hours each time
    sessions_per_day = 2 # twice a day
    hours_per_day_trained = hours_per_session * sessions_per_day

    # L2
    days_in_week = 7 # WK
    days_not_training = 2 # all but 2 days per week
    training_days_per_week = days_in_week - days_not_training

    # L3
    hours_per_week = hours_per_day_trained * training_days_per_week

    # L4
    weeks_per_year = 52 # WK
    total_hours_per_year = hours_per_week * weeks_per_year

    # FA
    answer = total_hours_per_year
    return answer