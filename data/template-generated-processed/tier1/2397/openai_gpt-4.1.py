def solve():
    """Index: 2397.
    Returns: the total number of hours Nathan and Tobias played baseball.
    """
    # L1
    days_per_week = 7 # WK
    nathan_weeks = 2 # two weeks
    nathan_days = nathan_weeks * days_per_week
    nathan_hours_per_day = 3 # played for 3 hours
    nathan_total_hours = nathan_hours_per_day * nathan_days

    # L2
    tobias_days = days_per_week # played for 7 days
    tobias_hours_per_day = 5 # played for 5 hours every day
    tobias_total_hours = tobias_hours_per_day * tobias_days

    # L3
    total_hours = nathan_total_hours + tobias_total_hours

    # FA
    answer = total_hours
    return answer