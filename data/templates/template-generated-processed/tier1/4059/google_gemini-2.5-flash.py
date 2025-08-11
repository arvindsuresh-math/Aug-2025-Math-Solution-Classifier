def solve():
    """Index: 4059.
    Returns: the total hours Mike trained during the first two weeks.
    """
    # L1
    days_per_week = 7 # WK
    hours_per_day_week1 = 2 # plays a maximum of 2 hours
    hours_trained_week1 = days_per_week * hours_per_day_week1

    # L2
    hours_per_day_week2 = 3 # increased the maximum time to 3 hours
    hours_trained_week2 = days_per_week * hours_per_day_week2

    # L3
    total_hours_trained = hours_trained_week2 + hours_trained_week1

    # FA
    answer = total_hours_trained
    return answer