def solve():
    """Index: 5919.
    Returns: the total minutes Janet will save every week.
    """
    # L1
    time_looking_for_keys = 8 # 8 minutes looking for her keys
    time_complaining = 3 # 3 minutes complaining
    daily_time_spent = time_looking_for_keys + time_complaining

    # L2
    days_in_week = 7 # WK
    weekly_time_saved = daily_time_spent * days_in_week

    # FA
    answer = weekly_time_saved
    return answer