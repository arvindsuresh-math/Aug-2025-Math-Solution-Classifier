def solve():
    """Index: 4729.
    Returns: the total distance the monkey will travel in feet.
    """
    # L1
    running_speed = 15 # speed of 15 feet per second
    running_time = 5 # runs for 5 seconds
    distance_running = running_time * running_speed

    # L2
    swinging_speed = 10 # speed of 10 feet per second
    swinging_time = 10 # swings for another 10 seconds
    distance_swinging = swinging_time * swinging_speed

    # L3
    total_distance = distance_running + distance_swinging

    # FA
    answer = total_distance
    return answer