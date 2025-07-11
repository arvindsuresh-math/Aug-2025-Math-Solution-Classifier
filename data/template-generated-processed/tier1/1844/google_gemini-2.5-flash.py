def solve():
    """Index: 1844.
    Returns: the number of hats that were unused.
    """
    # L1
    hats_per_bag = 15 # Each bag has 15 hats
    num_bags = 3 # 3 bags of birthday hats
    total_hats_initial = hats_per_bag * num_bags

    # L2
    hats_torn = 5 # tore off 5 hats
    hats_after_tear = total_hats_initial - hats_torn

    # L3
    hats_used = 25 # only 25 hats were used
    unused_hats = hats_after_tear - hats_used

    # FA
    answer = unused_hats
    return answer