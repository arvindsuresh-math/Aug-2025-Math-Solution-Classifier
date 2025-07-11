def solve():
    """Index: 2428.
    Returns: the total number of times Wilson sled down the hills.
    """
    # L1
    num_tall_hills = 2 # 2 tall hills
    times_per_tall_hill = 4 # 4 times each
    total_sleds_tall_hills = num_tall_hills * times_per_tall_hill

    # L2
    half_divisor = 2 # half as often
    times_per_small_hill = times_per_tall_hill / half_divisor

    # L3
    num_small_hills = 3 # 3 small hills
    total_sleds_small_hills = num_small_hills * times_per_small_hill

    # L4
    total_sleds = total_sleds_tall_hills + total_sleds_small_hills

    # FA
    answer = total_sleds
    return answer