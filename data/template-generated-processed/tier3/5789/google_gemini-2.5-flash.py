def solve():
    """Index: 5789.
    Returns: the combined total time Jonathan spends exercising in a week.
    """
    # L1
    distance_per_day = 6 # On each exercise day, he travels 6 miles
    speed_monday = 2 # walks at 2 miles per hour
    time_monday = distance_per_day / speed_monday

    # L2
    speed_wednesday = 3 # walks at 3 miles per hour
    time_wednesday = distance_per_day / speed_wednesday

    # L3
    speed_friday = 6 # runs at 6 miles per hour
    time_friday = distance_per_day / speed_friday

    # L4
    total_time = time_monday + time_wednesday + time_friday

    # FA
    answer = total_time
    return answer