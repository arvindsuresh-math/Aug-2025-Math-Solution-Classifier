def solve():
    """Index: 53.
    Returns: how much more Caleb spent on ice cream than on frozen yoghurt.
    """
    # L1
    num_ice_cream = 10 # 10 cartons of ice cream
    cost_per_ice_cream = 4 # each carton of ice cream cost $4
    total_ice_cream = num_ice_cream * cost_per_ice_cream

    # L2
    num_frozen_yoghurt = 4 # 4 cartons of frozen yoghurt
    cost_per_frozen_yoghurt = 1 # each carton of frozen yoghurt cost $1
    total_frozen_yoghurt = num_frozen_yoghurt * cost_per_frozen_yoghurt

    # L3
    difference = total_ice_cream - total_frozen_yoghurt

    # FA
    answer = difference
    return answer