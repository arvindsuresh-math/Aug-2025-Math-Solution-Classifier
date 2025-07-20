def solve():
    """Index: 5649.
    Returns: the total number of marbles Albert and Allison have.
    """
    # L1
    angela_more_than_allison = 8 # 8 more than Allison
    allison_marbles = 28 # who has 28 marbles
    angela_marbles = angela_more_than_allison + allison_marbles

    # L2
    albert_multiplier = 3 # three times as many marbles as Angela
    albert_marbles = albert_multiplier * angela_marbles

    # L3
    total_marbles_albert_allison = albert_marbles + allison_marbles

    # FA
    answer = total_marbles_albert_allison
    return answer