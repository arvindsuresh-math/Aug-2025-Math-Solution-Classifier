def solve():
    """Index: 2346.
    Returns: the total money that came out of John's pocket.
    """
    # L1
    old_system_cost = 250 # His old system cost 250 dollars
    trade_in_percentage = 0.8 # he got 80% of the value
    trade_in_value = old_system_cost * trade_in_percentage

    # L2
    new_system_cost = 600 # system that costs $600
    discount_percentage = 0.25 # 25% discount
    new_system_discount = new_system_cost * discount_percentage

    # L3
    final_new_system_cost = new_system_cost - new_system_discount

    # L4
    out_of_pocket_cost = final_new_system_cost - trade_in_value

    # FA
    answer = out_of_pocket_cost
    return answer