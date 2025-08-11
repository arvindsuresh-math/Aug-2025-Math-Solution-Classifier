def solve():
    """Index: 2807.
    Returns: the time Osborn needs to get dressed on Friday to tie his old weekly average.
    """
    # L1
    old_average_time = 3 # 3 minutes on average to get dressed
    school_days_in_week = 5 # WK
    total_time_old_method = school_days_in_week * old_average_time

    # L2
    monday_time = 2 # 2 minutes
    tuesday_time = 4 # 4 minutes
    wednesday_time = 3 # 3 minutes
    thursday_time = 4 # 4 minutes
    current_week_total_time = monday_time + tuesday_time + wednesday_time + thursday_time

    # L3
    friday_time_needed = total_time_old_method - current_week_total_time

    # FA
    answer = friday_time_needed
    return answer