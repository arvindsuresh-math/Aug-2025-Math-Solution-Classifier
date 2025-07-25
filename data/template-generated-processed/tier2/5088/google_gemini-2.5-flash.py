def solve():
    """Index: 5088.
    Returns: the amount Barbara spent on goods other than tuna and water.
    """
    # L1
    tuna_packs = 5 # 5 packs of tuna
    cost_per_tuna_pack = 2 # $2 each
    cost_tuna = tuna_packs * cost_per_tuna_pack

    # L2
    water_bottles = 4 # 4 bottles of water
    cost_per_water_bottle = 1.5 # $1.5 each
    cost_water = water_bottles * cost_per_water_bottle

    # L3
    total_paid = 56 # paid $56 for her shopping
    cost_other_goods = total_paid - cost_tuna - cost_water

    # FA
    answer = cost_other_goods
    return answer