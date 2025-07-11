def solve():
    """Index: 2713.
    Returns: the total space the trees will take up in the yard.
    """
    # L1
    num_apple_trees = 2 # 2 apple trees
    apple_tree_width = 10 # 10 feet wide each
    total_apple_width = num_apple_trees * apple_tree_width

    # L2
    space_between_apple_trees = 12 # 12 feet between them
    total_apple_space = total_apple_width + space_between_apple_trees

    # L3
    num_peach_trees = 2 # implied from 4 fruit trees total and 2 apple trees
    peach_tree_width = 12 # 12 feet wide
    total_peach_width = num_peach_trees * peach_tree_width

    # L4
    space_between_peach_trees = 15 # 15 feet between each tree
    total_peach_space = total_peach_width + space_between_peach_trees

    # L5
    total_space = total_apple_space + total_peach_space

    # FA
    answer = total_space
    return answer