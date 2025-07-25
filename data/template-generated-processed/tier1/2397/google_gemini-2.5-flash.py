def solve():
    """Index: 2397.
    Returns: the total hours Nathan and Tobias played.
    """
    # L1
    nathan_weeks = 2 # played for 3 hours for two weeks
    days_per_week = 7 # WK
    nathan_days = nathan_weeks * days_per_week
    nathan_hours_per_day = 3 # played for 3 hours
    nathan_total_hours = nathan_hours_per_day * nathan_days

    # L2
    tobias_hours_per_day = 5 # played for 5 hours
    tobias_weeks = 1 # only for one week
    tobias_days = tobias_weeks * days_per_week
    tobias_total_hours = tobias_hours_per_day * tobias_days

    # L3
    total_play_hours = nathan_total_hours + tobias_total_hours

    # FA
    answer = total_play_hours
    return answer