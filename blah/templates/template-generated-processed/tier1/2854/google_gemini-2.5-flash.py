def solve():
    """Index: 2854.
    Returns: the total minutes Javier and Sanda exercised.
    """
    # L1
    javier_daily_minutes = 50 # 50 minutes every day
    days_in_week = 7 # WK
    javier_total_minutes = javier_daily_minutes * days_in_week

    # L2
    sanda_daily_minutes = 90 # 90 minutes on each of three days
    sanda_num_days = 3 # three days
    sanda_total_minutes = sanda_daily_minutes * sanda_num_days

    # L3
    total_exercise_minutes = javier_total_minutes + sanda_total_minutes

    # FA
    answer = total_exercise_minutes
    return answer