def solve():
    """Index: 5560.
    Returns: the height of the smallest tree.
    """
    # L1
    tallest_tree_height = 108 # The tallest of 3 trees is 108 feet

    # L2
    half_divisor = 2 # half the height
    less_than_half = 6 # 6 feet less than half
    middle_tree_height = (tallest_tree_height / half_divisor) - less_than_half

    # L3
    quarter_divisor = 4 # 1/4 the height
    smallest_tree_height = middle_tree_height / quarter_divisor

    # FA
    answer = smallest_tree_height
    return answer