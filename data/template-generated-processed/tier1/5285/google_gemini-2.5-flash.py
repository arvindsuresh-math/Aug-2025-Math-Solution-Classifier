def solve():
    """Index: 5285.
    Returns: the number of birds in the trees.
    """
    # L1
    times_more = 3 # three times more
    number_of_stones = 40 # number of stones is 40
    more_trees_than_stones = times_more * number_of_stones

    # L2
    total_trees = more_trees_than_stones + number_of_stones

    # L3
    combined_trees_and_stones = total_trees + number_of_stones

    # L4
    multiplier_for_birds = 2 # twice as many birds
    total_birds = multiplier_for_birds * combined_trees_and_stones

    # FA
    answer = total_birds
    return answer