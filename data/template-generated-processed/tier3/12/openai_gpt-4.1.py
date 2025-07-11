def solve():
    """Index: 12.
    Returns: the total number of trees Randy has on his farm.
    """
    # L1
    mango_trees = 60 # Randy has 60 mango trees on his farm
    half_divisor = 2 # half as many coconut trees
    half_mango_trees = mango_trees / half_divisor

    # L2
    coconut_tree_difference = 5 # 5 less than half as many coconut trees
    coconut_trees = half_mango_trees - coconut_tree_difference

    # L3
    total_trees = mango_trees + coconut_trees

    # FA
    answer = total_trees
    return answer