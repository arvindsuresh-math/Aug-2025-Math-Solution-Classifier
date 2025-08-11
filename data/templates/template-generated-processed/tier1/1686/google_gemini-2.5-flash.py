def solve():
    """Index: 1686.
    Returns: the total number of hours Bob logs in a month.
    """
    # L1
    hours_per_day = 10 # 10 hours of work
    days_per_week = 5 # five days a week
    hours_per_week = hours_per_day * days_per_week

    # L2
    weeks_per_month = 4 # WK
    total_hours_per_month = weeks_per_month * hours_per_week

    # FA
    answer = total_hours_per_month
    return answer