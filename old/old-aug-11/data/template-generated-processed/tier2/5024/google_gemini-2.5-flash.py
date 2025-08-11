def solve():
    """Index: 5024.
    Returns: how far John can run now.
    """
    # L1
    initial_run_time = 8 # run 8 hours straight
    increase_percent = 0.75 # increases that by 75%
    time_increase_hours = initial_run_time * increase_percent

    # L2
    new_run_time = initial_run_time + time_increase_hours

    # L3
    initial_speed = 8 # speed of 8 mph
    speed_increase = 4 # by 4 mph
    new_speed = initial_speed + speed_increase

    # L4
    total_distance = new_run_time * new_speed

    # FA
    answer = total_distance
    return answer