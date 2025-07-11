def solve():
    """Index: 1979.
    Returns: the total number of seeds in a watermelon.
    """
    # L1
    slices_per_watermelon = 40 # 40 slices
    black_seeds_per_slice = 20 # 20 black seeds
    total_black_seeds = black_seeds_per_slice * slices_per_watermelon

    # L2
    white_seeds_per_slice = 20 # 20 white seeds
    total_white_seeds = white_seeds_per_slice * slices_per_watermelon

    # L3
    total_seeds = total_black_seeds + total_white_seeds

    # FA
    answer = total_seeds
    return answer