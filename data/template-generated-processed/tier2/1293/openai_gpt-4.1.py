def solve():
    """Index: 1293.
    Returns: the amount of money Jimmy and Irene give to the cashier.
    """
    # L1
    jimmy_shorts_qty = 3 # Jimmy picks out 3 shorts
    shorts_price = 15 # from the $15 rack
    jimmy_shorts_cost = jimmy_shorts_qty * shorts_price

    # L2
    irene_shirts_qty = 5 # Irene grabs 5 shirts
    shirts_price = 17 # from the $17 rack
    irene_shirts_cost = irene_shirts_qty * shirts_price

    # L3
    total_clothes_cost = jimmy_shorts_cost + irene_shirts_cost

    # L4
    discount_percent_num = 10 # 10% discount
    percent_factor = 0.01 # WK
    discount_amount = total_clothes_cost * discount_percent_num * percent_factor

    # L5
    answer = total_clothes_cost - discount_amount
    return answer