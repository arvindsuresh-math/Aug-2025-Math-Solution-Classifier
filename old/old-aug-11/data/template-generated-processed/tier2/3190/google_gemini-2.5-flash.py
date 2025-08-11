def solve():
    """Index: 3190.
    Returns: the total amount Neil will charge the customer.
    """
    # L1
    total_boxwoods = 30 # entire 30 boxwood hedge
    trim_cost_per_boxwood = 5.00 # $5.00 to trim up each boxwood
    total_trimming_cost = total_boxwoods * trim_cost_per_boxwood

    # L2
    num_shaped_boxwoods = 4 # 4 specific boxwoods shaped into spheres
    shape_cost_per_boxwood = 15.00 # $15.00 to trim it into a fancy shape
    total_shaping_cost = num_shaped_boxwoods * shape_cost_per_boxwood

    # L3
    total_charge = total_trimming_cost + total_shaping_cost

    # FA
    answer = total_charge
    return answer