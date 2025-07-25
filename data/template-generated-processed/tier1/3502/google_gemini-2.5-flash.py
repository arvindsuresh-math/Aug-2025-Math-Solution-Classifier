def solve():
    """Index: 3502.
    Returns: the total number of crickets Spike hunts per day.
    """
    # L1
    morning_crickets = 5 # 5 crickets every morning
    afternoon_evening_multiplier = 3 # three times that
    afternoon_evening_crickets = afternoon_evening_multiplier * morning_crickets

    # L2
    total_crickets_per_day = morning_crickets + afternoon_evening_crickets

    # FA
    answer = total_crickets_per_day
    return answer