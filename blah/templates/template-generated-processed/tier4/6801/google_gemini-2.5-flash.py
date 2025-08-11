def solve():
    """Index: 6801.
    Returns: the cost of a full tank of diesel fuel.
    """
    # L1
    total_cost_euros = 18 # €18
    total_liters = 36 # 36 liters of diesel fuel
    cost_per_liter = total_cost_euros / total_liters

    # L2
    tank_capacity_liters = 64 # can hold 64 liters
    full_tank_cost = cost_per_liter * tank_capacity_liters

    # FA
    answer = full_tank_cost
    return answer