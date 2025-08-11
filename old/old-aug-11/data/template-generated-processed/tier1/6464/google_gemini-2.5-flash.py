def solve():
    """Index: 6464.
    Returns: the total number of trees on the farm after planting.
    """
    # L1
    mahogany_initial = 50 # 50 Mahogany
    narra_initial = 30 # 30 Narra trees
    total_initial_trees = mahogany_initial + narra_initial

    # L2
    total_trees_fell = 5 # a total of 5 trees fell
    mahogany_fell_more_than_narra = 1 # One more Mahogany tree fell than the number of Narra trees that fell
    narra_fell = int((total_trees_fell - mahogany_fell_more_than_narra) / 2)
    mahogany_fell = narra_fell + mahogany_fell_more_than_narra

    # L3
    multiplier_narra_planted = 2 # twice as much as the number of the Narra
    narra_planted = narra_fell * multiplier_narra_planted

    # L4
    multiplier_mahogany_planted = 3 # thrice the number of Mahogany trees that fell
    mahogany_planted = mahogany_fell * multiplier_mahogany_planted

    # L5
    total_trees_planted = narra_planted + mahogany_planted

    # L6
    trees_after_typhoon = total_initial_trees - total_trees_fell

    # L7
    final_total_trees = trees_after_typhoon + total_trees_planted

    # FA
    answer = final_total_trees
    return answer