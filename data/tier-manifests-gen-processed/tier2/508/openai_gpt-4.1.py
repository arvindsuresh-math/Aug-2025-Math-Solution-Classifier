def solve():
    """Index: 508.
    Returns: the total distance James drove.
    """
    # L1
    first_speed = 30 # drives 30 mph
    first_duration = 0.5 # half an hour
    first_distance = first_speed * first_duration

    # L2
    next_leg_multiplier = 2 # twice as long
    next_duration = first_duration * next_leg_multiplier

    # L3
    speed_multiplier = 2 # twice the speed
    next_speed = first_speed * speed_multiplier

    # L4
    next_distance = next_speed * next_duration

    # L5
    total_distance = next_distance + first_distance

    # FA
    answer = total_distance
    return answer