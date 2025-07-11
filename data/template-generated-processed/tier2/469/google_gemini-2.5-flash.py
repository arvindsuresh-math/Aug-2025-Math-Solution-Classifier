def solve():
    """Index: 469.
    Returns: the total amount Jackson spends on champagne.
    """
    # L1
    hot_tub_gallons = 40 # hot tub holds 40 gallons of liquid
    quarts_per_gallon = 4 # WK
    hot_tub_quarts = hot_tub_gallons * quarts_per_gallon

    # L2
    cost_per_bottle = 50 # each bottle of champagne costs $50
    cost_before_discount = hot_tub_quarts * cost_per_bottle

    # L3
    volume_discount_percent_text = 20 # 20% volume discount
    volume_discount_decimal = 0.2 # 20% volume discount
    discount_amount = cost_before_discount * volume_discount_decimal

    # L4
    final_cost = cost_before_discount - discount_amount

    # FA
    answer = final_cost
    return answer