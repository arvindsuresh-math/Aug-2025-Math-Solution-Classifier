def solve():
    """Index: 1014.
    Returns: the total distance Hazel walked for 2 hours.
    """
    # L1
    distance_first_hour = 2 # 2 kilometers in the first hour
    multiplier_second_hour = 2 # twice as far
    distance_second_hour = distance_first_hour * multiplier_second_hour

    # L2
    total_distance = distance_first_hour + distance_second_hour

    # FA
    answer = total_distance
    return answer