def solve():
    """Index: 2767.
    Returns: the total number of minutes Polly spends cooking this week.
    """
    # L1
    breakfast_minutes_per_day = 20 # 20 minutes to cook breakfast every day
    days_in_week = 7 # WK
    breakfast_total = breakfast_minutes_per_day * days_in_week

    # L2
    lunch_minutes_per_day = 5 # 5 minutes cooking lunch
    lunch_total = lunch_minutes_per_day * days_in_week

    # L3
    dinner_minutes_short = 10 # 10 minutes cooking dinner
    dinner_short_days = 4 # 4 days this week
    dinner_minutes_long = 30 # 30 minutes cooking dinner
    dinner_long_days = days_in_week - dinner_short_days
    dinner_total = (dinner_minutes_short * dinner_short_days) + (dinner_minutes_long * dinner_long_days)

    # L4
    total_minutes = breakfast_total + lunch_total + dinner_total

    # FA
    answer = total_minutes
    return answer