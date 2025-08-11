def solve():
    """Index: 6290.
    Returns: the height of the shortest tree.
    """
    # L1
    tallest_tree_height = 150 # The tallest tree is 150 feet tall

    # L2
    middle_tree_fraction_numerator = 2 # 2/3 the height of the tallest tree
    middle_tree_fraction_denominator = 3 # 2/3 the height of the tallest tree
    intermediate_product = tallest_tree_height * middle_tree_fraction_numerator
    middle_tree_height = intermediate_product / middle_tree_fraction_denominator

    # L3
    shortest_tree_divisor = 2 # half the size of the middle tree
    shortest_tree_height = middle_tree_height / shortest_tree_divisor

    # FA
    answer = shortest_tree_height
    return answer