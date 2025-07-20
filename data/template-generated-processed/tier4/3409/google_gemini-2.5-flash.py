def solve():
    """Index: 3409.
    Returns: the total amount Peter spends on soda.
    """
    # L1
    total_ounces_needed = 80 # 80 ounces of soda
    ounces_per_can = 8 # 8 oz cans
    num_cans_needed = total_ounces_needed / ounces_per_can

    # L2
    cost_per_can = 0.5 # $.5 each
    total_cost = num_cans_needed * cost_per_can

    # FA
    answer = total_cost
    return answer