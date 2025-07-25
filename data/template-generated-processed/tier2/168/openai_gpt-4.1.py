def solve():
    """Index: 168.
    Returns: the total cost of Silvia's order with the discount applied.
    """
    # L1
    num_quiches = 2 # 2 quiches
    quiche_price = 15.00 # $15.00 each
    quiche_total = num_quiches * quiche_price

    # L2
    num_croissants = 6 # 6 croissants
    croissant_price = 3.00 # $3.00 each
    croissant_total = num_croissants * croissant_price

    # L3
    num_biscuits = 6 # 6 biscuits
    biscuit_price = 2.00 # $2.00 each
    biscuit_total = num_biscuits * biscuit_price

    # L4
    order_total = quiche_total + croissant_total + biscuit_total

    # L5
    discount_percent_decimal = 0.10 # .10*60
    discount_amount = discount_percent_decimal * order_total

    # L6
    final_total = order_total - discount_amount

    # FA
    answer = final_total
    return answer