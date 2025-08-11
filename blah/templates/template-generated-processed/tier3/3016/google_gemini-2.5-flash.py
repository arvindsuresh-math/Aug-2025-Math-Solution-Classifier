def solve():
    """Index: 3016.
    Returns: the total amount Gary spends on chlorine.
    """
    # L1
    pool_length = 10 # 10 feet long
    pool_width = 8 # 8 feet wide
    pool_depth = 6 # 6 feet deep
    pool_volume = pool_length * pool_width * pool_depth

    # L2
    cubic_feet_per_quart = 120 # one quart of chlorine for every 120 cubic feet
    quarts_needed = pool_volume / cubic_feet_per_quart

    # L3
    cost_per_quart = 3 # chlorine costs $3 a quart
    total_cost = cost_per_quart * quarts_needed

    # FA
    answer = total_cost
    return answer