def solve():
    """Index: 6116.
    Returns: the total weight of pine cones on Alan's roof in ounces.
    """
    # L1
    num_trees = 8 # 8 pine trees
    pine_cones_per_tree = 200 # each tree drops 200 pine cones
    total_pine_cones = num_trees * pine_cones_per_tree

    # L2
    percent_on_roof_num = 30 # 30% of the pine cones
    percent_factor = 0.01 # WK
    pine_cones_on_roof = total_pine_cones * percent_on_roof_num * percent_factor

    # L3
    weight_per_pine_cone = 4 # each pine cone weighs 4 ounces
    total_weight_on_roof = pine_cones_on_roof * weight_per_pine_cone

    # FA
    answer = total_weight_on_roof
    return answer