def solve():
    """Index: 729.
    Returns: the total distance John will have traveled.
    """
    # L1
    dog_run_speed = 6 # runs at 6 miles per hour when with dog
    dog_run_time = 0.5 # 30 minutes = 0.5 hours
    dog_run_distance = dog_run_speed * dog_run_time

    # L2
    solo_run_speed = 4 # runs at 4 miles per hour when alone
    solo_run_time = 0.5 # additional 30 minutes = 0.5 hours
    solo_run_distance = solo_run_speed * solo_run_time

    # L3
    total_distance = dog_run_distance + solo_run_distance

    # FA
    answer = total_distance
    return answer