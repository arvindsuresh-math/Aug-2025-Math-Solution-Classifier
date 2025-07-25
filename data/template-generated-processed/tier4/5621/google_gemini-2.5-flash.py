def solve():
    """Index: 5621.
    Returns: the number of hours Lawrence would work each day if he worked the same number of hours each day.
    """
    # L1
    hours_per_day_mon_tue_fri = 8 # 8 hours each day on Monday, Tuesday and Friday
    num_days_mon_tue_fri = 3 # Monday, Tuesday and Friday
    total_hours_mon_tue_fri = hours_per_day_mon_tue_fri * num_days_mon_tue_fri

    # L2
    hours_per_day_wed_thu = 5.5 # 5.5 hours on both Wednesday and Thursday
    num_days_wed_thu = 2 # both Wednesday and Thursday
    total_hours_wed_thu = hours_per_day_wed_thu * num_days_wed_thu

    # L3
    total_hours_week = total_hours_mon_tue_fri + total_hours_wed_thu

    # L4
    days_in_week = 7 # WK
    average_hours_per_day = total_hours_week / days_in_week

    # FA
    answer = average_hours_per_day
    return answer