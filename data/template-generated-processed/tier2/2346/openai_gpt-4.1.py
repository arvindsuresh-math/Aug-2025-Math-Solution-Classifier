def solve():
    """Index: 2346.
    Returns: the amount of money John paid out of pocket for the new stereo system.
    """
    # L1
    old_system_cost = 250 # old system cost 250 dollars
    trade_in_percent = 0.8 # got 80% of the value for it
    trade_in_value = old_system_cost * trade_in_percent

    # L2
    new_system_cost = 600 # system that costs $600
    discount_percent = 0.25 # 25% discount
    discount_amount = new_system_cost * discount_percent

    # L3
    discounted_price = new_system_cost - discount_amount

    # L4
    out_of_pocket = discounted_price - trade_in_value

    # FA
    answer = out_of_pocket
    return answer