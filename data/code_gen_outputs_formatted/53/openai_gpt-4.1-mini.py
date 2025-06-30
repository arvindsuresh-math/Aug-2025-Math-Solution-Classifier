def solve(
    cartons_ice_cream: int = 10,  # Caleb bought 10 cartons of ice cream
    cartons_frozen_yoghurt: int = 4,  # and 4 cartons of frozen yoghurt
    cost_per_ice_cream: int = 4,  # Each carton of ice cream cost $4
    cost_per_frozen_yoghurt: int = 1  # Each carton of frozen yoghurt cost $1
):
    """Index: 53.
    Returns: how much more Caleb spent on ice cream than on frozen yoghurt.
    """

    #: L1
    total_cost_ice_cream = cartons_ice_cream * cost_per_ice_cream

    #: L2
    total_cost_frozen_yoghurt = cartons_frozen_yoghurt * cost_per_frozen_yoghurt

    #: L3
    difference = total_cost_ice_cream - total_cost_frozen_yoghurt

    #: FA
    answer = difference
    return answer