def solve():
    """Index: 6020.
    Returns: the amount Carrie pays for the clothes.
    """
    # L1
    num_shirts = 4 # 4 shirts
    cost_per_shirt = 8 # Each shirt costs $8
    total_cost_shirts = num_shirts * cost_per_shirt

    # L2
    num_pants = 2 # 2 pairs of pants
    cost_per_pant = 18 # Each pair of pants costs $18
    total_cost_pants = num_pants * cost_per_pant

    # L3
    num_jackets = 2 # 2 jackets
    cost_per_jacket = 60 # Each jacket costs $60
    total_cost_jackets = num_jackets * cost_per_jacket

    # L4
    total_cost_all_clothes = total_cost_shirts + total_cost_pants + total_cost_jackets

    # L5
    mom_pays_divisor = 2 # half of the total cost
    carrie_pays = total_cost_all_clothes / mom_pays_divisor

    # FA
    answer = carrie_pays
    return answer