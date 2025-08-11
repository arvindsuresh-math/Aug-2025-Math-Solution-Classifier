def solve():
    """Index: 5812.
    Returns: the total liters of oil the store owner had.
    """
    # L1
    bottle_capacity_ml = 200 # 200 mL bottles
    num_bottles = 20 # 20 bottles
    total_volume_ml = bottle_capacity_ml * num_bottles

    # L2
    ml_per_liter = 1000 # 1 liter is equal to 1000 mL
    total_volume_liters = total_volume_ml / ml_per_liter

    # FA
    answer = total_volume_liters
    return answer