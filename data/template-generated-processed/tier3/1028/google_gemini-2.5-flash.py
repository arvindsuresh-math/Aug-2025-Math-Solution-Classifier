def solve():
    """Index: 1028.
    Returns: the total weight of a container with 20 bars of each type of metal.
    """
    # L1
    num_bars_per_type = 20 # 20 bars of each type of metal
    copper_bar_weight = 90 # a copper bar weighs 90 kgs
    total_copper_weight = num_bars_per_type * copper_bar_weight

    # L2
    steel_more_than_copper = 20 # weighs 20 kgs more than a copper bar
    steel_bar_weight = copper_bar_weight + steel_more_than_copper

    # L3
    total_steel_weight = num_bars_per_type * steel_bar_weight

    # L4
    total_copper_steel_weight = total_steel_weight + total_copper_weight

    # L5
    steel_tin_ratio = 2 # twice the mass
    tin_bar_weight = steel_bar_weight / steel_tin_ratio

    # L6
    total_tin_weight = tin_bar_weight * num_bars_per_type

    # L7
    total_container_weight = total_copper_steel_weight + total_tin_weight

    # FA
    answer = total_container_weight
    return answer