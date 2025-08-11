def solve():
    """Index: 2941.
    Returns: the total distance Francine drives to work for 4 weeks.
    """
    # L1
    days_in_week = 7 # WK
    days_not_at_work_per_week = 3 # 3 days every week
    days_at_work_per_week = days_in_week - days_not_at_work_per_week

    # L2
    distance_per_day = 140 # drives 140km to work each day
    distance_per_week = distance_per_day * days_at_work_per_week

    # L3
    num_weeks = 4 # for 4 weeks
    total_distance = num_weeks * distance_per_week

    # FA
    answer = total_distance
    return answer