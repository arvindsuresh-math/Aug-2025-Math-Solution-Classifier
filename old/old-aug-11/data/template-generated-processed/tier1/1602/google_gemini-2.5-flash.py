def solve():
    """Index: 1602.
    Returns: the remaining distance Amelia has to drive.
    """
    # L1
    distance_monday = 907 # drove 907 kilometers on Monday
    distance_tuesday = 582 # and 582 kilometers on Tuesday
    distance_driven = distance_monday + distance_tuesday

    # L2
    total_distance_across_country = 8205 # The distance across a country is 8205 kilometers
    distance_remaining = total_distance_across_country - distance_driven

    # FA
    answer = distance_remaining
    return answer