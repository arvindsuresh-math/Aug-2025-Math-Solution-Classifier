def solve():
    """Index: 7260.
    Returns: the total number of birds in the park.
    """
    # L1
    num_trees = 7 # park’s 7 trees
    blackbirds_per_tree = 3 # 3 blackbirds in each
    total_blackbirds = num_trees * blackbirds_per_tree

    # L2
    num_magpies = 13 # 13 magpies roaming around the park
    total_birds = total_blackbirds + num_magpies

    # FA
    answer = total_birds
    return answer