def solve():
    """Index: 1557.
    Returns: the number of minutes Jenna can tan in the last two weeks of the month.
    """
    # L1
    tan_minutes_per_day = 30 # tans 30 minutes a day
    tan_days_per_week = 2 # two days a week
    minutes_tanned_per_week = tan_minutes_per_day * tan_days_per_week

    # L2
    initial_weeks_tanning = 2 # for the first two weeks of the month
    minutes_tanned_first_half_month = minutes_tanned_per_week * initial_weeks_tanning

    # L3
    max_tan_minutes_per_month = 200 # tan no more than 200 minutes a month
    remaining_tan_minutes = max_tan_minutes_per_month - minutes_tanned_first_half_month

    # FA
    answer = remaining_tan_minutes
    return answer