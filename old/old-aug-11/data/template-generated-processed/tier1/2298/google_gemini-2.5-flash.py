def solve():
    """Index: 2298.
    Returns: the number of seeds planted in the fourth pot.
    """
    # L1
    num_pots_filled_initially = 3 # 3 pots
    seeds_per_pot = 3 # 3 seeds can be planted in 1 pot
    total_seeds_in_three_pots = num_pots_filled_initially * seeds_per_pot

    # L2
    total_seeds_eunice_has = 10 # 10 eggplant seeds
    remaining_seeds = total_seeds_eunice_has - total_seeds_in_three_pots

    # FA
    answer = remaining_seeds
    return answer