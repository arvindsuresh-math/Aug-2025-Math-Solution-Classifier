def solve():
    """Index: 5196.
    Returns: the total time Mark wants to spend reading books weekly.
    """
    # L1
    reading_hours_per_day = 2 # 2 hours each day
    days_in_week = 7 # WK
    current_weekly_reading_hours = reading_hours_per_day * days_in_week

    # L2
    increase_weekly_hours = 4 # by 4 hours
    goal_weekly_reading_hours = current_weekly_reading_hours + increase_weekly_hours

    # FA
    answer = goal_weekly_reading_hours
    return answer