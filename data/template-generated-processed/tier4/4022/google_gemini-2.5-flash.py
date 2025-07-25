def solve():
    """Index: 4022.
    Returns: the number of hours James spends meditating per week.
    """
    # L1
    minutes_per_session = 30 # 30 minutes
    minutes_per_hour = 60 # WK
    hours_per_session = minutes_per_session / minutes_per_hour

    # L2
    sessions_per_day = 2 # twice a day
    hours_per_day = hours_per_session * sessions_per_day

    # L3
    days_per_week = 7 # WK
    hours_per_week = hours_per_day * days_per_week

    # FA
    answer = hours_per_week
    return answer