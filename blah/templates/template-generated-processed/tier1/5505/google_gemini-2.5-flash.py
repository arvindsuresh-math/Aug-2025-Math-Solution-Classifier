def solve():
    """Index: 5505.
    Returns: the number of caterpillars left on the tree.
    """
    # L1
    initial_caterpillars = 14 # 14 caterpillars on the tree
    new_eggs_hatch = 4 # 4 more eggs hatch
    caterpillars_after_hatch = initial_caterpillars + new_eggs_hatch

    # L2
    fat_caterpillars_leave = 8 # 8 fat caterpillars leave the tree
    caterpillars_left = caterpillars_after_hatch - fat_caterpillars_leave

    # FA
    answer = caterpillars_left
    return answer