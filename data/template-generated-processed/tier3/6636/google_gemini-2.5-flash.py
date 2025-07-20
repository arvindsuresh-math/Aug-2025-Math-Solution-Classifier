def solve():
    """Index: 6636.
    Returns: the total number of seeds the newest plants will produce.
    """
    # L1
    total_seeds_produced = 50 # 50 fluffy, white seeds
    half_divisor = 2 # Only half of these seeds
    germinated_seeds = total_seeds_produced / half_divisor

    # L2
    seeds_per_plant = 50 # produces the same number of seeds
    total_new_seeds_produced = germinated_seeds * seeds_per_plant

    # FA
    answer = total_new_seeds_produced
    return answer