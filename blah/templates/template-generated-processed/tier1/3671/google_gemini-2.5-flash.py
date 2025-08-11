def solve():
    """Index: 3671.
    Returns: the total time it will take Diana to get home.
    """
    # L1
    time_fast_speed = 2 # two hours
    speed_fast = 3 # 3 mph
    distance_fast = time_fast_speed * speed_fast

    # L2
    total_distance = 10 # 10 miles to get home
    remaining_distance = total_distance - distance_fast

    # L3
    speed_slow = 1 # 1 mph
    time_slow_speed = remaining_distance * speed_slow

    # L4
    total_time = time_fast_speed + time_slow_speed

    # FA
    answer = total_time
    return answer