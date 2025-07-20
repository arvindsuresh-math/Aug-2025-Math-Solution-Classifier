def solve():
    """Index: 6878.
    Returns: the number of strawberry seeds remaining.
    """
    # L1
    seeds_per_zone = 3123 # 3123 seeds will be used
    num_planting_zones = 7 # 7 planting zones
    total_seeds_used = seeds_per_zone * num_planting_zones

    # L2
    initial_seeds = 54000 # Lolita has 54000 strawberry seeds
    remaining_seeds = initial_seeds - total_seeds_used

    # FA
    answer = remaining_seeds
    return answer