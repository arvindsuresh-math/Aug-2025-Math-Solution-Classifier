def solve():
    """Index: 3901.
    Returns: the number of additional seeds Steven needs to fulfill his assignment.
    """
    # L1
    num_apples = 4 # 4 apples
    seeds_per_apple = 6 # Apples average 6 seeds
    apple_seeds = num_apples * seeds_per_apple

    # L2
    num_pears = 3 # 3 pears
    seeds_per_pear = 2 # pears average 2 seeds
    pear_seeds = num_pears * seeds_per_pear

    # L3
    num_grapes = 9 # 9 grapes
    seeds_per_grape = 3 # grapes average 3 seeds
    grape_seeds = num_grapes * seeds_per_grape

    # L4
    total_collected_seeds = apple_seeds + pear_seeds + grape_seeds

    # L5
    target_seeds = 60 # collect 60 different fruit seeds
    seeds_needed = target_seeds - total_collected_seeds

    # FA
    answer = seeds_needed
    return answer