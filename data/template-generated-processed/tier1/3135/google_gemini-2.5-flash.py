def solve():
    """Index: 3135.
    Returns: the total cost to fill the pool.
    """
    # L1
    pool_depth = 10 # 10 feet deep
    pool_width = 6 # 6 feet by 20 feet
    pool_length = 20 # 6 feet by 20 feet
    pool_volume_cubic_feet = pool_depth * pool_width * pool_length

    # L2
    liters_per_cubic_foot = 25 # A cubic foot of water is 25 liters
    pool_volume_liters = liters_per_cubic_foot * pool_volume_cubic_feet

    # L3
    cost_per_liter = 3 # A liter of water costs $3
    total_cost = cost_per_liter * pool_volume_liters

    # FA
    answer = total_cost
    return answer