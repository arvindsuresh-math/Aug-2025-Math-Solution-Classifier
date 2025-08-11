def solve():
    """Index: 1880.
    Returns: the total miles Milo can run.
    """
    # L1
    cory_speed = 12 # Cory always drives his wheelchair at 12 miles per hour
    cory_milo_speed_ratio = 2 # Cory, can drive his wheelchair at twice the speed that Milo can roll downhill on his skateboard
    milo_skateboard_speed = cory_speed / cory_milo_speed_ratio

    # L2
    milo_skateboard_run_ratio = 2 # Milo can roll downhill on his skateboard at twice the speed that he can run
    milo_run_speed = milo_skateboard_speed / milo_skateboard_run_ratio

    # L3
    run_time = 2 # two hours
    milo_run_distance = run_time * milo_run_speed

    # FA
    answer = milo_run_distance
    return answer