def solve(
        num_ice_cream_cartons: int = 10, # 10 cartons of ice cream
        num_frozen_yogurt_cartons: int = 4, # 4 cartons of frozen yoghurt
        cost_per_ice_cream_carton: int = 4, # Each carton of ice cream cost $4
        cost_per_frozen_yogurt_carton: int = 1 # each carton of frozen yoghurt cost $1
    ):
    """Index: 53.
    Returns: how much more Caleb spent on ice cream than on frozen yoghurt.
    """

    #: L1
    cost_ice_cream = num_ice_cream_cartons * cost_per_ice_cream_carton

    #: L2
    cost_frozen_yogurt = num_frozen_yogurt_cartons * cost_per_frozen_yogurt_carton

    #: L3
    difference_in_cost = cost_ice_cream - cost_frozen_yogurt

    answer = difference_in_cost # FINAL ANSWER
    return answer