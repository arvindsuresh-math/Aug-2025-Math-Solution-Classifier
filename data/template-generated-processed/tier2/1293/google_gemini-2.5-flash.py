def solve():
    """Index: 1293.
    Returns: the total amount of money given to the cashier.
    """
    # L1
    num_shorts = 3 # 3 shorts
    cost_per_short = 15 # $15 rack
    jimmy_shorts_cost = num_shorts * cost_per_short

    # L2
    num_shirts = 5 # 5 shirts
    cost_per_shirt = 17 # $17 rack
    irene_shirts_cost = num_shirts * cost_per_shirt

    # L3
    total_initial_cost = jimmy_shorts_cost + irene_shirts_cost

    # L4
    discount_percent_num = 10 # 10% discount
    percent_factor = 0.01 # WK
    discount_amount = total_initial_cost * discount_percent_num * percent_factor

    # L5
    final_cost = total_initial_cost - discount_amount

    # FA
    answer = final_cost
    return answer