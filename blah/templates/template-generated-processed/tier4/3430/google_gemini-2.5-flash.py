def solve():
    """Index: 3430.
    Returns: the number of hours her father sleeps in a week.
    """
    # L1
    samantha_sleep_hours_day = 8 # 8 hours a night
    baby_sleep_multiplier = 2.5 # 2.5 times as much as Samantha does
    baby_sleep_hours_day = baby_sleep_multiplier * samantha_sleep_hours_day

    # L2
    minutes_per_hour = 60 # WK
    father_sleep_minutes_per_baby_hour = 30 # he sleeps 30 minutes
    baby_sleep_multiplier_relative_to_father = minutes_per_hour / father_sleep_minutes_per_baby_hour

    # L3
    father_sleep_hours_day = baby_sleep_hours_day / baby_sleep_multiplier_relative_to_father

    # L4
    days_per_week = 7 # WK
    father_sleep_hours_week = days_per_week * father_sleep_hours_day

    # FA
    answer = father_sleep_hours_week
    return answer