def solve():
    """Index: 7376.
    Returns: the number of beef jerky pieces Janette will have left.
    """
    # L1
    breakfast_jerky = 1 # 1 for breakfast
    lunch_jerky = 1 # 1 for lunch
    dinner_jerky = 2 # 2 for dinner
    daily_jerky_consumption = breakfast_jerky + lunch_jerky + dinner_jerky

    # L2
    trip_duration_days = 5 # camping for 5 days
    total_jerky_consumed = daily_jerky_consumption * trip_duration_days

    # L3
    brother_share_divisor = 2 # giving half of the remaining pieces to her brother
    jerky_left_after_sharing = total_jerky_consumed / brother_share_divisor

    # FA
    answer = jerky_left_after_sharing
    return answer