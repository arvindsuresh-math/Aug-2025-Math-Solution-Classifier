def solve():
    """Index: 4476.
    Returns: the total number of trees planted.
    """
    # L1
    peach_multiplier = 3 # 3 times as many peaches as apricots
    apricot_trees_planted = 58 # 58 apricot trees were planted
    peach_trees_planted = peach_multiplier * apricot_trees_planted

    # L2
    total_trees_planted = peach_trees_planted + apricot_trees_planted

    # FA
    answer = total_trees_planted
    return answer