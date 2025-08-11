def solve():
    """Index: 1422.
    Returns: the total number of accidents that will happen.
    """
    # L1
    seconds_per_minute = 60 # WK
    duration_minutes = 4 # in 4 minutes
    total_seconds = duration_minutes * seconds_per_minute

    # L2
    big_crash_interval = 20 # every 20 seconds there is a big crash
    num_big_crashes = total_seconds / big_crash_interval

    # L3
    car_collision_interval = 10 # Every 10 seconds, there is a car collision
    num_car_collisions = total_seconds / car_collision_interval

    # L4
    total_accidents = num_big_crashes + num_car_collisions

    # FA
    answer = total_accidents
    return answer