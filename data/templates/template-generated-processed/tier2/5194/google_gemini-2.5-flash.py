def solve():
    """Index: 5194.
    Returns: Sean's net profit.
    """
    # L1
    num_patches = 100 # orders his patches in a unit of 100
    cost_per_patch = 1.25 # charged $1.25 per patch
    total_cost_patches = num_patches * cost_per_patch

    # L2
    sell_price_per_patch = 12.00 # sells all 100 patches for $12.00 each
    total_revenue = num_patches * sell_price_per_patch

    # L3
    net_profit = total_revenue - total_cost_patches

    # FA
    answer = net_profit
    return answer