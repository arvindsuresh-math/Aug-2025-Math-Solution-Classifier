def solve():
    """Index: 6873.
    Returns: the total number of plants in the garden.
    """
    # L1
    oregano_more = 2 # 2 more than twice as many oregano plants
    oregano_multiplier = 2 # twice as many oregano plants
    basil_plants = 5 # 5 basil plants
    oregano_plants = oregano_more + oregano_multiplier * basil_plants

    # L2
    total_plants = oregano_plants + basil_plants

    # FA
    answer = total_plants
    return answer