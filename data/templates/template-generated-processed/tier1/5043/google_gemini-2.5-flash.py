def solve():
    """Index: 5043.
    Returns: the total number of trees in the forest.
    """
    # L1
    street_side_length = 100 # length of 100 meters on one side
    street_area = street_side_length * street_side_length

    # L2
    forest_area_multiplier = 3 # three times the area
    forest_area = forest_area_multiplier * street_area

    # L3
    trees_per_sq_meter = 4 # number of trees per square meter in the forest is 4
    total_trees = trees_per_sq_meter * forest_area

    # FA
    answer = total_trees
    return answer