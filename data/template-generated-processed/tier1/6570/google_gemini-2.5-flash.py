def solve():
    """Index: 6570.
    Returns: the total time James spends painting.
    """
    # L1
    time_per_space_marine = 20 # 20 minutes to paint a space marine
    num_space_marines = 6 # paints 6 space marines
    total_time_space_marines = time_per_space_marine * num_space_marines

    # L2
    time_per_dreadnought = 70 # 70 minutes to paint a dreadnought
    num_dreadnoughts = 2 # paints 2 dreadnoughts
    total_time_dreadnoughts = time_per_dreadnought * num_dreadnoughts

    # L3
    total_painting_time = total_time_space_marines + total_time_dreadnoughts

    # FA
    answer = total_painting_time
    return answer