def solve(
    num_ice_cream_cartons: int = 10, # Caleb bought 10 cartons of ice cream
    num_frozen_yoghurt_cartons: int = 4, # and 4 cartons of frozen yoghurt
    cost_per_ice_cream_carton: int = 4, # Each carton of ice cream cost $4
    cost_per_frozen_yoghurt_carton: int = 1 # and each carton of frozen yoghurt cost $1
):
    """Index: 53.
    Returns: the difference in cost between ice cream and frozen yoghurt.
    """
    #: L1
    cost_ice_cream = num_ice_cream_cartons * cost_per_ice_cream_carton # eval: 40 = 10 * 4
    #: L2
    cost_frozen_yoghurt = num_frozen_yoghurt_cartons * cost_per_frozen_yoghurt_carton # eval: 4 = 4 * 1
    #: L3
    difference_in_cost = cost_ice_cream - cost_frozen_yoghurt # eval: 36 = 40 - 4
    answer = difference_in_cost # FINAL ANSWER # eval: 36 = 36 # FINAL ANSWER
    return answer # eval: return 36