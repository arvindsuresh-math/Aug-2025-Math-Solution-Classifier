def solve():
    """Index: 1792.
    Returns: the total number of flowers needed to fill the order.
    """
    # L1
    snapdragons_per_arrangement = 3 # 3 snapdragons
    lilies_multiplier = 2 # twice as many lilies
    lilies_per_arrangement = lilies_multiplier * snapdragons_per_arrangement

    # L2
    roses_per_arrangement = 8 # 8 roses
    daisies_per_arrangement = 12 # 12 daisies
    flowers_per_arrangement = roses_per_arrangement + daisies_per_arrangement + snapdragons_per_arrangement + lilies_per_arrangement

    # L3
    tables = 10 # 10 tables
    total_flowers = flowers_per_arrangement * tables

    # FA
    answer = total_flowers
    return answer