def solve():
    """Index: 5769.
    Returns: the number of goats Zara owns.
    """
    # L1
    num_groups = 3 # 3 equally-sized groups
    animals_per_group = 48 # 48 animals per group
    total_animals = num_groups * animals_per_group

    # L2
    num_cows = 24 # 24 cows
    num_sheep = 7 # 7 sheep
    known_animals = num_cows + num_sheep

    # L3
    num_goats = total_animals - known_animals

    # FA
    answer = num_goats
    return answer