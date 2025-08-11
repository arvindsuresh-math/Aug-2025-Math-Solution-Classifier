def solve():
    """Index: 469.
    Returns: the total amount Jackson spends on champagne for the hot tub.
    """
    # L1
    tub_gallons = 40 # hot tub holds 40 gallons
    quarts_per_gallon = 4 # 4 quarts per gallon
    total_quarts = tub_gallons * quarts_per_gallon

    # L2
    price_per_bottle = 50 # $50 per bottle (1 quart per bottle)
    pre_discount_cost = total_quarts * price_per_bottle

    # L3
    discount_percent = 0.2 # 20% volume discount
    discount_amount = pre_discount_cost * discount_percent

    # L4
    final_cost = pre_discount_cost - discount_amount

    # FA
    answer = final_cost
    return answer