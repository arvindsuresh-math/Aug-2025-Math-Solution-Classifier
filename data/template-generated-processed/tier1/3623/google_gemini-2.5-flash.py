def solve():
    """Index: 3623.
    Returns: the total time Mark spends on all activities in a week.
    """
    # L1
    parking_time_per_day = 5 # 5 minutes to find parking
    walking_time_per_day = 3 # 3 minutes to walk into the courthouse
    daily_parking_walking_time = parking_time_per_day + walking_time_per_day

    # L2
    work_days_per_week = 5 # 5 work days
    total_parking_walking_time_per_week = daily_parking_walking_time * work_days_per_week

    # L3
    long_wait_days = 2 # 2 days of the week
    long_wait_time_per_day = 30 # 30 minutes to get through the metal detector
    total_long_wait_time_per_week = long_wait_days * long_wait_time_per_day

    # L4
    short_wait_days = 3 # the other 3 days
    short_wait_time_per_day = 10 # 10 minutes
    total_short_wait_time_per_week = short_wait_days * short_wait_time_per_day

    # L5
    total_time_spent_per_week = total_short_wait_time_per_week + total_long_wait_time_per_week + total_parking_walking_time_per_week

    # FA
    answer = total_time_spent_per_week
    return answer