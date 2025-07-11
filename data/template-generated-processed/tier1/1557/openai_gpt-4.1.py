def solve():
    """Index: 1557.
    Returns: the number of minutes Jenna can tan in the last two weeks of the month.
    """
    # L1
    minutes_per_day = 30 # 30 minutes a day
    days_per_week = 2 # two days a week
    minutes_per_week = minutes_per_day * days_per_week

    # L2
    weeks_first_half = 2 # first two weeks of the month
    minutes_first_half = minutes_per_week * weeks_first_half

    # L3
    max_minutes_per_month = 200 # no more than 200 minutes a month
    minutes_last_half = max_minutes_per_month - minutes_first_half

    # FA
    answer = minutes_last_half
    return answer