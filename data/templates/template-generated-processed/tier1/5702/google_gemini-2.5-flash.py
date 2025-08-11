def solve():
    """Index: 5702.
    Returns: the amount of change Donny will get.
    """
    # L1
    tank_capacity = 150 # truck holds 150 liters of fuel
    already_contained = 38 # truck already contained 38 liters
    liters_needed = tank_capacity - already_contained

    # L2
    cost_per_liter = 3 # each liter of fuel costs $3
    total_cost = liters_needed * cost_per_liter

    # L3
    money_given = 350 # get from $350
    change_received = money_given - total_cost

    # FA
    answer = change_received
    return answer