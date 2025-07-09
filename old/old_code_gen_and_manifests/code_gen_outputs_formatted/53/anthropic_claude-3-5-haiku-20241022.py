def solve(
    num_ice_cream_cartons: int = 10,  # Caleb bought 10 cartons of ice cream
    num_yoghurt_cartons: int = 4,  # and 4 cartons of frozen yoghurt
    cost_per_ice_cream_carton: int = 4,  # Each carton of ice cream cost $4
    cost_per_yoghurt_carton: int = 1  # each carton of frozen yoghurt cost $1
):
    """Index: 53.
    Returns: the difference in amount spent on ice cream versus frozen yoghurt."""

    #: L1
    total_ice_cream_cost = num_ice_cream_cartons * cost_per_ice_cream_carton

    #: L2
    total_yoghurt_cost = num_yoghurt_cartons * cost_per_yoghurt_carton

    #: L3
    difference_in_cost = total_ice_cream_cost - total_yoghurt_cost

    #: FA
    answer = difference_in_cost
    return answer