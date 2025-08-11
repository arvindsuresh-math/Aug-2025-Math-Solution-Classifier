def solve():
    """Index: 1884.
    Returns: the total weight of the bag.
    """
    # L1
    bag_capacity = 250 # 250 pound sandbag
    fill_percentage = 0.8 # 80% full
    sand_weight = bag_capacity * fill_percentage

    # L2
    heavier_percentage = 0.4 # 40% heavier
    heavier_amount = sand_weight * heavier_percentage

    # L3
    total_weight = sand_weight + heavier_amount

    # FA
    answer = total_weight
    return answer