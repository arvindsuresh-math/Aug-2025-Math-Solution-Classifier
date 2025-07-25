def solve():
    """Index: 3242.
    Returns: the difference in spending between ice cream and pudding.
    """
    # L1
    num_ice_cream_cones = 15 # 15 ice cream cones
    cost_per_ice_cream_cone = 5 # Each ice cream cone cost $5
    total_cost_ice_cream = num_ice_cream_cones * cost_per_ice_cream_cone

    # L2
    num_pudding_cups = 5 # 5 cups of pudding
    cost_per_pudding_cup = 2 # each cup of pudding cost $2
    total_cost_pudding = num_pudding_cups * cost_per_pudding_cup

    # L3
    difference_in_spending = total_cost_ice_cream - total_cost_pudding

    # FA
    answer = difference_in_spending
    return answer