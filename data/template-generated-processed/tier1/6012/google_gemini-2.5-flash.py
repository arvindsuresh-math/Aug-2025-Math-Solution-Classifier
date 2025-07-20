def solve():
    """Index: 6012.
    Returns: the final height of the tree.
    """
    # L1
    boy_final_height = 36 # by the time the boy is 36 inches tall
    boy_initial_height = 24 # the boy was 24 inches tall
    boy_growth = boy_final_height - boy_initial_height

    # L2
    tree_growth_multiplier = 2 # grows twice as fast
    tree_growth = boy_growth * tree_growth_multiplier

    # L3
    tree_initial_height = 16 # planted a 16-inch tree
    tree_final_height = tree_initial_height + tree_growth

    # FA
    answer = tree_final_height
    return answer