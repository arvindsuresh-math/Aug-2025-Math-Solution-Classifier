def solve():
    """Index: 2727.
    Returns: the number of small planters needed to plant all basil seeds.
    """
    # L1
    num_large_planters = 4 # 4 large planters
    seeds_per_large_planter = 20 # can hold 20 seeds each
    total_seeds_large_planters = num_large_planters * seeds_per_large_planter

    # L2
    initial_basil_seeds = 200 # Oshea bought 200 basil seeds
    remaining_seeds = initial_basil_seeds - total_seeds_large_planters

    # L3
    seeds_per_small_planter = 4 # small planters that can hold 4 seeds each
    num_small_planters_needed = remaining_seeds / seeds_per_small_planter

    # FA
    answer = num_small_planters_needed
    return answer