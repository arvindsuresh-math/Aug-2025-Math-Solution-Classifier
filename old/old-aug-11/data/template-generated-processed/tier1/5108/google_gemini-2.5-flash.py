def solve():
    """Index: 5108.
    Returns: the cost of the burger.
    """
    # L1
    num_packs_fries = 2 # two packs of fries
    price_per_pack_fries = 2 # one pack of fries was for $2
    cost_fries = num_packs_fries * price_per_pack_fries

    # L2
    salad_price_multiplier = 3 # three times that price
    cost_salad = salad_price_multiplier * price_per_pack_fries

    # L3
    total_paid = 15 # paid in total $15
    cost_burger = total_paid - cost_salad - cost_fries

    # FA
    answer = cost_burger
    return answer