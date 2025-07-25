def solve():
    """Index: 2593.
    Returns: the total number of animals on the farm after the transaction.
    """
    # L1
    cows = 12 # 12 cows
    sheep_per_cow = 2 # twice as many sheep
    sheep = sheep_per_cow * cows

    # L2
    pigs_per_sheep = 3 # 3 pigs for every sheep
    pigs = pigs_per_sheep * sheep

    # L3
    total_animals = pigs + sheep + cows

    # FA
    answer = total_animals
    return answer