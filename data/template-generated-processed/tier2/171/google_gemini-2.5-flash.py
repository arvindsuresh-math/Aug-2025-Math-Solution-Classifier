def solve():
    """Index: 171.
    Returns: the number of trees James planted.
    """
    # L1
    plants_per_tree = 20 # Each tree has 20 plants
    num_trees = 2 # his 2 trees
    total_seeds = plants_per_tree * num_trees

    # L2
    planting_percentage = 0.6 # plants 60% of those
    trees_planted = total_seeds * planting_percentage

    # FA
    answer = trees_planted
    return answer