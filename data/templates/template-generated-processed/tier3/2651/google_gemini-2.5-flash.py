def solve():
    """Index: 2651.
    Returns: the minimum number of trees Felix has chopped down.
    """
    # L1
    total_sharpening_cost = 35 # If he spends $35 on axe sharpening
    cost_per_sharpening = 5 # It cost him $5 to sharpen his axe
    num_sharpenings = total_sharpening_cost / cost_per_sharpening

    # L2
    trees_per_sharpening = 13 # For every 13 trees he chops down
    total_trees_chopped = num_sharpenings * trees_per_sharpening

    # FA
    answer = total_trees_chopped
    return answer