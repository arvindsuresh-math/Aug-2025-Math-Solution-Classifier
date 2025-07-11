def solve():
    """Index: 496.
    Returns: the original number of matchsticks Michael had.
    """
    # L1
    num_houses = 30 # he creates 30 matchstick houses
    matchsticks_per_house = 10 # each matchstick house uses 10 matchsticks
    matchsticks_used = num_houses * matchsticks_per_house

    # L2
    fraction_used = 2 # only used half, so multiply by 2 to get original
    original_matchsticks = matchsticks_used * fraction_used

    # FA
    answer = original_matchsticks
    return answer