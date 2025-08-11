def solve():
    """Index: 2713.
    Returns: the total space (in feet) the trees will take up in Quinton's yard.
    """
    # L1
    num_apple_trees = 2 # 2 apple trees
    apple_tree_width = 10 # 10 feet wide each
    total_apple_width = num_apple_trees * apple_tree_width

    # L2
    apple_spacing = 12 # 12 feet between them
    apple_total_space = total_apple_width + apple_spacing

    # L3
    num_peach_trees = 2 # 2 peach trees
    peach_tree_width = 12 # 12 feet wide
    total_peach_width = num_peach_trees * peach_tree_width

    # L4
    peach_spacing = 15 # 15 feet between each tree
    peach_total_space = total_peach_width + peach_spacing

    # L5
    total_space = apple_total_space + peach_total_space

    # FA
    answer = total_space
    return answer