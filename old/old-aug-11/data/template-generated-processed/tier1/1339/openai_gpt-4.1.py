def solve():
    """Index: 1339.
    Returns: the total amount the plumber spent on copper and plastic pipe.
    """
    # L1
    copper_meters = 10 # 10 meters of copper
    plastic_more_than_copper = 5 # 5 more meters of plastic pipe
    plastic_meters = copper_meters + plastic_more_than_copper

    # L2
    total_meters = copper_meters + plastic_meters

    # L3
    cost_per_meter = 4 # each meter cost $4
    total_cost = cost_per_meter * total_meters

    # FA
    answer = total_cost
    return answer