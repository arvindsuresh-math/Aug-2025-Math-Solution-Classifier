def solve():
    """Index: 2767.
    Returns: the total minutes Polly spends cooking this week.
    """
    # L1
    breakfast_daily_minutes = 20 # 20 minutes to cook breakfast every day
    days_in_week = 7 # WK
    breakfast_total_minutes = breakfast_daily_minutes * days_in_week

    # L2
    lunch_daily_minutes = 5 # 5 minutes cooking lunch
    lunch_total_minutes = lunch_daily_minutes * days_in_week

    # L3
    dinner_special_days_minutes = 10 # 10 minutes cooking dinner
    dinner_special_days_count = 4 # 4 days this week
    dinner_other_days_minutes = 30 # 30 minutes cooking dinner
    dinner_other_days_count = days_in_week - dinner_special_days_count # The rest of the days
    dinner_total_minutes = (dinner_special_days_minutes * dinner_special_days_count) + (dinner_other_days_minutes * dinner_other_days_count)

    # L4
    total_cooking_minutes_week = breakfast_total_minutes + lunch_total_minutes + dinner_total_minutes

    # FA
    answer = total_cooking_minutes_week
    return answer