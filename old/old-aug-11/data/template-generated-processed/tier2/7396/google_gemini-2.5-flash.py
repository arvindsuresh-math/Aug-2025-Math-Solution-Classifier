def solve():
    """Index: 7396.
    Returns: the money a restaurant makes on a bottle of spirits.
    """
    # L1
    servings_per_bottle = 16 # 16 servings per bottle
    charge_per_serving = 8.00 # $8.00 for one serving
    revenue_per_bottle = servings_per_bottle * charge_per_serving

    # L2
    cost_per_bottle = 30.00 # $30.00
    profit_per_bottle = revenue_per_bottle - cost_per_bottle

    # FA
    answer = profit_per_bottle
    return answer