def solve():
    """Index: 5268.
    Returns: the total number of pools both stores have.
    """
    # L1
    athletic_wear_pools = 200 # Pat's Ark & Athletic Wear store has 200 pools
    multiplier_pool_supply = 3 # three times as many swimming pools
    pool_supply_pools = multiplier_pool_supply * athletic_wear_pools

    # L2
    total_pools = pool_supply_pools + athletic_wear_pools

    # FA
    answer = total_pools
    return answer