def solve():
    """Index: 3869.
    Returns: the number of hours of sleep Tom is behind on from the last week.
    """
    # L1
    ideal_sleep_per_night = 8 # 8 hours of sleep each night
    days_in_week = 7 # WK
    ideal_total_sleep = ideal_sleep_per_night * days_in_week

    # L2
    actual_sleep_weeknight = 5 # 5 hours of sleep each weeknight
    weeknights_per_week = 5 # WK
    actual_sleep_weeknights_total = actual_sleep_weeknight * weeknights_per_week

    # L3
    actual_sleep_weekend_night = 6 # 6 hours each night on the weekend
    weekend_nights_per_week = 2 # WK
    actual_sleep_weekend_total = actual_sleep_weekend_night * weekend_nights_per_week

    # L4
    actual_total_sleep = actual_sleep_weeknights_total + actual_sleep_weekend_total

    # L5
    sleep_deficit = ideal_total_sleep - actual_total_sleep

    # FA
    answer = sleep_deficit
    return answer