def solve():
    """Index: 1884.
    Returns: the weight of the sandbag with the heavier filling material.
    """
    # L1
    full_bag_weight = 250 # 250 pound sandbag
    fill_percent = 0.8 # 80% full
    sand_weight = full_bag_weight * fill_percent

    # L2
    heavier_percent = 0.4 # 40% heavier than sand
    extra_weight = sand_weight * heavier_percent

    # L3
    total_weight = sand_weight + extra_weight

    # FA
    answer = total_weight
    return answer