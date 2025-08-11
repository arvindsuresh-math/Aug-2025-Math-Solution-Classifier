def solve():
    """Index: 2298.
    Returns: the number of seeds planted in the fourth pot.
    """
    # L1
    pots_for_full_planting = 3 # 3 pots
    seeds_per_pot = 3 # 3 seeds can be planted in 1 pot
    seeds_in_three_pots = pots_for_full_planting * seeds_per_pot

    # L2
    total_seeds = 10 # Eunice has 10 eggplant seeds
    seeds_in_fourth_pot = total_seeds - seeds_in_three_pots

    # FA
    answer = seeds_in_fourth_pot
    return answer