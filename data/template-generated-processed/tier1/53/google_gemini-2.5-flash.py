def solve():
    """Index: 53.
    Returns: how much more Caleb spent on ice cream than on frozen yoghurt.
    """
    # L1
    num_ice_cream_cartons = 10 # 10 cartons of ice cream
    cost_per_ice_cream_carton = 4 # Each carton of ice cream cost $4
    cost_of_ice_cream = num_ice_cream_cartons * cost_per_ice_cream_carton

    # L2
    num_yogurt_cartons = 4 # 4 cartons of frozen yoghurt
    cost_per_yogurt_carton = 1 # each carton of frozen yoghurt cost $1
    cost_of_frozen_yogurt = num_yogurt_cartons * cost_per_yogurt_carton

    # L3
    difference_in_cost = cost_of_ice_cream - cost_of_frozen_yogurt

    # FA
    answer = difference_in_cost
    return answer