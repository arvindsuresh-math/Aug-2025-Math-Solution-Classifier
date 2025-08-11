def solve():
    """Index: 3597.
    Returns: the total number of oranges picked.
    """
    # L1
    oranges_tree1 = 80 # 80 oranges from one tree
    oranges_tree2 = 60 # 60 from another tree
    oranges_after_two_trees = oranges_tree1 + oranges_tree2

    # L2
    oranges_tree3 = 120 # 120 from the third tree
    total_oranges = oranges_after_two_trees + oranges_tree3

    # FA
    answer = total_oranges
    return answer