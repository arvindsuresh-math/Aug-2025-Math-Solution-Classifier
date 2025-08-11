def solve():
    """Index: 3927.
    Returns: the total time in minutes to travel the full mile.
    """
    # L1
    run_distance = 0.5 # half a mile
    run_speed = 3 # 3 miles per hour
    minutes_per_hour = 60 # WK
    hours_per_hour = 1 # WK
    time_to_run = run_distance / run_speed * minutes_per_hour

    # L2
    walk_distance = 0.5 # half a mile
    walk_speed = 1 # 1 mile per hour
    time_to_walk = walk_distance / walk_speed * minutes_per_hour

    # L3
    total_time = time_to_run + time_to_walk

    # FA
    answer = total_time
    return answer