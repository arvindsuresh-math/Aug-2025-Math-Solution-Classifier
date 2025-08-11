def solve():
    """Index: 335.
    Returns: the total amount Eve will spend on the gifts.
    """
    # L1
    utensils_cost = 10.00 # a set of 3 cooking utensils is $10.00
    knife_multiplier = 2 # a small knife is twice the amount of the utensils
    knife_cost = knife_multiplier * utensils_cost

    # L2
    mitts_cost = 14.00 # hand mitts cost $14.00
    apron_cost = 16.00 # apron is $16.00
    kit_total_cost = mitts_cost + apron_cost + utensils_cost + knife_cost

    # L3
    discount_percent = 0.25 # 25% off sale
    kit_discount = kit_total_cost * discount_percent

    # L4
    discounted_kit_cost = kit_total_cost - kit_discount

    # L5
    num_kits = 3 # 3 nieces
    total_cost = num_kits * discounted_kit_cost

    # FA
    answer = total_cost
    return answer