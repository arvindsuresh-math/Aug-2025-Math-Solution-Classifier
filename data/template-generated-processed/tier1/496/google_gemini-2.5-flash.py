def solve():
    """Index: 496.
    Returns: the original number of matchsticks Michael had.
    """
    # L1
    num_houses = 30 # 30 matchsticks houses
    matchsticks_per_house = 10 # each matchstick house uses 10 matchsticks
    matchsticks_used = num_houses * matchsticks_per_house

    # L2
    half_multiplier = 2 # only use half of his pile of matchsticks
    original_matchsticks = matchsticks_used * half_multiplier

    # FA
    answer = original_matchsticks
    return answer