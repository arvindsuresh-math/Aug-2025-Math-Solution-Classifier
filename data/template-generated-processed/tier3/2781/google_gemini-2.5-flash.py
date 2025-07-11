def solve():
    """Index: 2781.
    Returns: the time it took Amy to finish the race.
    """
    # L1
    patrick_finish_time = 60 # Patrick finishes the race in 60 seconds
    manu_extra_time = 12 # Manu took 12 more seconds
    manu_total_time = patrick_finish_time + manu_extra_time

    # L2
    amy_time_numerator = 1 # If Amy is twice as fast as Manu
    amy_time_divisor = 2 # If Amy is twice as fast as Manu
    amy_time = (amy_time_numerator / amy_time_divisor) * manu_total_time

    # FA
    answer = amy_time
    return answer