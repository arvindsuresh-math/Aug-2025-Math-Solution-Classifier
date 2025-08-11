def solve():
    """Index: 2947.
    Returns: the total distance the two rabbits will hop in 5 minutes.
    """
    # L1
    white_rabbit_speed = 15 # 15 meters in one minute
    brown_rabbit_speed = 12 # 12 meters per minute
    combined_speed = white_rabbit_speed + brown_rabbit_speed

    # L2
    time_in_minutes = 5 # 5 minutes
    total_distance = time_in_minutes * combined_speed

    # FA
    answer = total_distance
    return answer