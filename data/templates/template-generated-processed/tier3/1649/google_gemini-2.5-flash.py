def solve():
    """Index: 1649.
    Returns: the number of clovers that are both purple and four-leaved.
    """
    # L1
    total_clovers = 500 # In a field of 500 clovers
    four_leaf_clover_divisor = 5 # 20% have four leaves
    four_leaf_clovers = total_clovers / four_leaf_clover_divisor

    # L2
    purple_clover_divisor = 4 # one quarter of these are purple clovers
    purple_four_leaf_clovers = four_leaf_clovers / purple_clover_divisor

    # FA
    answer = purple_four_leaf_clovers
    return answer