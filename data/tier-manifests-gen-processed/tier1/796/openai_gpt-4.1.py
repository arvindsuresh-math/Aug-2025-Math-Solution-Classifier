def solve():
    """Index: 796.
    Returns: the total time it takes Carla to cook 3 steaks and a batch of waffles.
    """
    # L1
    num_steaks = 3 # 3 steaks
    steak_time = 6 # chicken-fried steak in 6 minutes
    total_steak_time = num_steaks * steak_time

    # L2
    waffle_time = 10 # batch of waffles in 10 minutes
    total_time = total_steak_time + waffle_time

    # FA
    answer = total_time
    return answer