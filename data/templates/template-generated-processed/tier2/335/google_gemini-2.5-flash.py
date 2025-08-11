def solve():
    """Index: 335.
    Returns: the total amount Eve will spend on the gifts.
    """
    # L1
    utensils_cost = 10.00 # A set of 3 cooking utensils is $10.00
    knife_multiplier = 2 # a small knife is twice the amount
    knife_cost = knife_multiplier * utensils_cost

    # L2
    hand_mitts_cost = 14.00 # The hand mitts cost $14.00
    apron_cost = 16.00 # the apron is $16.00
    cost_per_kit_before_discount = hand_mitts_cost + apron_cost + utensils_cost + knife_cost

    # L3
    discount_percent_num = 25 # 25% off sale
    discount_percent_decimal = 0.25 # 25% off sale
    discount_amount_per_kit = cost_per_kit_before_discount * discount_percent_decimal

    # L4
    cost_per_kit_after_discount = cost_per_kit_before_discount - discount_amount_per_kit

    # L5
    num_nieces = 3 # buy her 3 nieces
    total_cost = num_nieces * cost_per_kit_after_discount

    # FA
    answer = total_cost
    return answer