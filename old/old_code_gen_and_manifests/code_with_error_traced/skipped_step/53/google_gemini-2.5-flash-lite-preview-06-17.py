def solve(
    num_ice_cream_cartons: int = 10, # Caleb bought 10 cartons of ice cream
    num_yogurt_cartons: int = 4, # and 4 cartons of frozen yoghurt
    cost_ice_cream_carton: int = 4, # Each carton of ice cream cost $4
    cost_yogurt_carton: int = 1 # and each carton of frozen yoghurt cost $1
):
    """Index: 53.
    Returns: the difference in cost between ice cream and frozen yoghurt.
    """

    #: L1
    cost_ice_cream = num_ice_cream_cartons * cost_ice_cream_carton # eval: 40 = 10 * 4

    #: L2

    #: L3
    difference_in_cost = cost_ice_cream - num_yogurt_cartons # eval: 36 = 40 - 4

    #: FA
    answer = difference_in_cost
    return answer # eval: return 36
