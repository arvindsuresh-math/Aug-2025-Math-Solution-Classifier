def solve():
    """Index: 2450.
    Returns: the number of rungs Jamie has to climb this time.
    """
    # L1
    rungs_climbed_last_time = 12 # had to climb 12 rungs
    tree_height_last_time = 6 # from a 6-foot tree
    rungs_per_foot = rungs_climbed_last_time / tree_height_last_time

    # L2
    current_tree_height = 20 # a 20-foot tree
    total_rungs_needed = current_tree_height * rungs_per_foot

    # FA
    answer = total_rungs_needed
    return answer