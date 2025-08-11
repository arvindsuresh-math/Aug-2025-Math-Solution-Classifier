def solve():
    """Index: 6407.
    Returns: the percentage chance of picking a peanut cluster.
    """
    # L1
    caramels = 3 # 3 of them were caramels
    nougat_multiplier = 2 # twice as many were nougats
    nougats = caramels * nougat_multiplier

    # L2
    truffle_addition = 6 # plus 6
    truffles = caramels + truffle_addition

    # L3
    total_chocolates = 50 # box of 50 chocolates
    peanut_clusters = total_chocolates - caramels - nougats - truffles

    # L4
    percentage_multiplier = 100 # 100%
    percentage_chance = (peanut_clusters / total_chocolates) * percentage_multiplier

    # FA
    answer = percentage_chance
    return answer