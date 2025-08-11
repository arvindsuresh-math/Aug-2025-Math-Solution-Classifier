def solve():
    """Index: 7388.
    Returns: how much less Yella's computer usage is for this week compared to last week.
    """
    # L1
    hours_per_day_this_week = 8 # 8 hours a day for this week
    days_in_week = 7 # WK
    usage_this_week = hours_per_day_this_week * days_in_week

    # L2
    usage_last_week = 91 # 91 hours
    difference = usage_last_week - usage_this_week

    # FA
    answer = difference
    return answer