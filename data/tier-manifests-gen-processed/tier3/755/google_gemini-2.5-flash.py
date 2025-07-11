def solve():
    """Index: 755.
    Returns: the total number of miles covered.
    """
    # L1
    swim_time = 2 # 2 hours
    swim_speed = 2 # 2 miles per hour
    swimming_distance = swim_time * swim_speed

    # L2
    run_time_divisor = 2 # half the time
    running_time = swim_time / run_time_divisor

    # L3
    speed_multiplier = 4 # 4 times the speed
    running_speed = swim_speed * speed_multiplier

    # L4
    running_distance = running_speed * running_time

    # L5
    total_distance = running_distance + swimming_distance

    # FA
    answer = total_distance
    return answer