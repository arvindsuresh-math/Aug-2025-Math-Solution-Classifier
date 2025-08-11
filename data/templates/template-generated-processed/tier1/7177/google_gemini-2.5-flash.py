def solve():
    """Index: 7177.
    Returns: the total number of insects eaten.
    """
    # L1
    num_geckos = 5 # 5 geckos
    insects_per_gecko = 6 # eat 6 insects each
    insects_eaten_by_geckos = num_geckos * insects_per_gecko

    # L2
    num_lizards = 3 # 3 lizards
    multiplier_for_lizards = 2 # twice as much as the geckos
    insects_per_lizard = insects_per_gecko * multiplier_for_lizards
    insects_eaten_by_lizards = num_lizards * insects_per_lizard

    # L3
    total_insects_eaten = insects_eaten_by_geckos + insects_eaten_by_lizards

    # FA
    answer = total_insects_eaten
    return answer