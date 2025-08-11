def solve():
    """Index: 2593.
    Returns: the total number of animals on the farm after the transaction.
    """
    # L1
    sheep_multiplier = 2 # twice as many sheep
    num_cows = 12 # 12 cows
    num_sheep = sheep_multiplier * num_cows

    # L2
    pigs_per_sheep = 3 # 3 pigs for every sheep
    num_pigs = pigs_per_sheep * num_sheep

    # L3
    total_animals = num_pigs + num_sheep + num_cows

    # FA
    answer = total_animals
    return answer