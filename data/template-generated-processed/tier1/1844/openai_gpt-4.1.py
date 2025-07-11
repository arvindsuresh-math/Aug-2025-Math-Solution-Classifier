def solve():
    """Index: 1844.
    Returns: the number of unused hats after the party.
    """
    # L1
    hats_per_bag = 15 # Each bag has 15 hats
    num_bags = 3 # 3 bags
    total_hats = hats_per_bag * num_bags

    # L2
    hats_torn = 5 # Miggy accidentally tore off 5 hats
    hats_left = total_hats - hats_torn

    # L3
    hats_used = 25 # only 25 hats were used
    hats_unused = hats_left - hats_used

    # FA
    answer = hats_unused
    return answer