def solve():
    """Index: 6627.
    Returns: the total amount of sleep John got this week.
    """
    # L1
    days_with_low_sleep = 2 # 2 of the days
    hours_low_sleep_per_day = 3 # 3 hours of sleep
    total_low_sleep_hours = days_with_low_sleep * hours_low_sleep_per_day

    # L2
    days_in_week = 7 # WK
    remaining_days = days_in_week - days_with_low_sleep

    # L3
    recommended_sleep_hours = 8 # recommended 8 hours of sleep
    percentage_of_recommended_sleep = 0.6 # 60% of the recommended
    sleep_per_remaining_day = recommended_sleep_hours * percentage_of_recommended_sleep

    # L4
    total_remaining_sleep_hours = remaining_days * sleep_per_remaining_day

    # L5
    total_sleep_this_week = total_remaining_sleep_hours + total_low_sleep_hours

    # FA
    answer = total_sleep_this_week
    return answer