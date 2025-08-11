def solve():
    """Index: 796.
    Returns: the total time to cook 3 steaks and a batch of waffles.
    """
    # L1
    num_steaks = 3 # 3 steaks
    time_per_steak = 6 # chicken-fried steak in 6 minutes
    total_steak_time = num_steaks * time_per_steak

    # L2
    time_per_waffles = 10 # a batch of waffles in 10 minutes
    total_cook_time = total_steak_time + time_per_waffles

    # FA
    answer = total_cook_time
    return answer