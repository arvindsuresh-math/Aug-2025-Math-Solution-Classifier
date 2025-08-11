def solve():
    """Index: 7002.
    Returns: the latest time Liz can start roasting the turkeys.
    """
    # L1
    minutes_per_pound = 15 # 15 minutes per pound
    turkey_weight = 16 # 16 pounds turkeys
    time_per_turkey_minutes = minutes_per_pound * turkey_weight

    # L2
    num_turkeys = 2 # 2 16 pounds turkeys
    total_cooking_time_minutes = num_turkeys * time_per_turkey_minutes

    # L3
    minutes_per_hour = 60 # WK
    total_cooking_time_hours = total_cooking_time_minutes / minutes_per_hour

    # L4
    dinner_time_pm_hour = 6 # 6:00 pm
    hours_in_half_day = 12 # WK
    start_time_am_hour = (dinner_time_pm_hour + hours_in_half_day) - total_cooking_time_hours

    # FA
    answer = start_time_am_hour
    return answer