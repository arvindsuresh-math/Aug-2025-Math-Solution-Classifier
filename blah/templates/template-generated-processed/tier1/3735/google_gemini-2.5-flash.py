def solve():
    """Index: 3735.
    Returns: the total number of birds Camille saw.
    """
    # L1
    cardinals = 3 # 3 cardinals
    multiplier_robins = 4 # four times as many robins
    num_robins = cardinals * multiplier_robins

    # L2
    multiplier_blue_jays = 2 # twice as many blue jays
    num_blue_jays = cardinals * multiplier_blue_jays

    # L3
    multiplier_triple = 3 # three times as many sparrows
    triple_cardinals = cardinals * multiplier_triple

    # L4
    sparrow_plus_one = 1 # 1 more than three times as many sparrows
    num_sparrows = triple_cardinals + sparrow_plus_one

    # L5
    total_birds = cardinals + num_robins + num_blue_jays + num_sparrows

    # FA
    answer = total_birds
    return answer