def solve():
    """Index: 5908.
    Returns: the total number of hours spent cleaning trees.
    """
    # L1
    trees_row = 4 # 4 trees by 5 trees
    trees_col = 5 # 4 trees by 5 trees
    total_trees = trees_row * trees_col

    # L2
    minutes_per_tree = 6 # 6 minutes to clean each tree
    total_minutes_original = total_trees * minutes_per_tree

    # L3
    minutes_per_hour = 60 # WK
    total_hours_original = total_minutes_original / minutes_per_hour

    # L4
    help_divisor = 2 # half as long
    actual_hours_spent = total_hours_original / help_divisor

    # FA
    answer = actual_hours_spent
    return answer