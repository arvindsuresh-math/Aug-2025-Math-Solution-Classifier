def solve():
    """Index: 2481.
    Returns: the number of mangoes each neighbor receives.
    """
    # L1
    total_mangoes = 560 # 560 mangoes
    sold_fraction_denominator = 2 # sold half of it
    mangoes_left_after_selling = total_mangoes / sold_fraction_denominator

    # L2
    num_neighbors = 8 # 8 of his neighbors
    mangoes_per_neighbor = mangoes_left_after_selling / num_neighbors

    # FA
    answer = mangoes_per_neighbor
    return answer