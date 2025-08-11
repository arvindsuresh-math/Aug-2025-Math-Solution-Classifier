def solve():
    """Index: 6222.
    Returns: the total number of mascots Jina has.
    """
    # L1
    initial_teddies = 5 # She has 5 teddies
    bunnies_multiplier = 3 # 3 times more bunnies
    initial_bunnies = initial_teddies * bunnies_multiplier

    # L2
    additional_teddies_per_bunny = 2 # two additional teddies for every bunny she has
    additional_teddies_from_mom = initial_bunnies * additional_teddies_per_bunny

    # L3
    koala_bear = 1 # a koala bear
    total_mascots = initial_teddies + initial_bunnies + koala_bear + additional_teddies_from_mom

    # FA
    answer = total_mascots
    return answer