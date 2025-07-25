def solve():
    """Index: 6190.
    Returns: the total amount of more sleep Angela got in January.
    """
    # L1
    january_sleep_hours_per_night = 8.5 # 8.5 hours a night in January
    december_sleep_hours_per_night = 6.5 # 6.5 hours every night in December
    daily_sleep_increase = january_sleep_hours_per_night - december_sleep_hours_per_night

    # L2
    days_in_month = 31 # 31 days in December and January
    total_sleep_increase = daily_sleep_increase * days_in_month

    # FA
    answer = total_sleep_increase
    return answer