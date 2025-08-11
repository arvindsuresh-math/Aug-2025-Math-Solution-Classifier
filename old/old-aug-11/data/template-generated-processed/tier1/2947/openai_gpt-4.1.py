def solve():
    """Index: 2947.
    Returns: the total distance the two rabbits will hop in 5 minutes.
    """
    # L1
    white_rabbit_per_min = 15 # can hop 15 meters in one minute
    brown_rabbit_per_min = 12 # hops 12 meters per minute
    combined_per_min = white_rabbit_per_min + brown_rabbit_per_min

    # L2
    minutes = 5 # in 5 minutes
    total_distance = minutes * combined_per_min

    # FA
    answer = total_distance
    return answer