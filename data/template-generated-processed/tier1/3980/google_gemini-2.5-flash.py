def solve():
    """Index: 3980.
    Returns: the total number of birds in the crape myrtle tree.
    """
    # L1
    swallows = 2 # If there were 2 swallows
    multiplier_for_bluebirds = 2 # half as many swallows as bluebirds (implies bluebirds are twice swallows)
    bluebirds = swallows * multiplier_for_bluebirds

    # L2
    cardinal_multiplier = 3 # three times more cardinals than bluebirds
    cardinals = cardinal_multiplier * bluebirds

    # L3
    total_birds = swallows + bluebirds + cardinals

    # FA
    answer = total_birds
    return answer