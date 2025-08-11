def solve():
    """Index: 6105.
    Returns: the total number of leaves falling from the trees.
    """
    # L1
    original_planned_trees = 7 # originally intended to plant 7 cherry trees
    multiplier_twice = 2 # twice as many cherry trees
    total_cherry_trees = original_planned_trees * multiplier_twice

    # L2
    leaves_per_tree = 100 # Each tree drops 100 leaves
    total_leaves = total_cherry_trees * leaves_per_tree

    # FA
    answer = total_leaves
    return answer