def solve():
    """Index: 3751.
    Returns: the total distance the monkey will swing in meters.
    """
    # L1
    avg_distance_per_second = 1.2 # average distance of 1.2 meters per second
    seconds_per_minute = 60 # WK
    distance_per_minute = avg_distance_per_second * seconds_per_minute

    # L2
    total_minutes = 30 # for 30 minutes
    total_distance_swung = distance_per_minute * total_minutes

    # FA
    answer = total_distance_swung
    return answer