def solve():
    """Index: 5771.
    Returns: the total cost of all items.
    """
    # L1
    shirts_bought = 10 # James buys 10 shirts
    pants_divisor = 2 # half as many pants
    pants_bought = shirts_bought / pants_divisor

    # L2
    shirt_cost_each = 6 # The shirts cost $6 each
    total_shirt_cost = shirts_bought * shirt_cost_each

    # L3
    pant_cost_each = 8 # the pants cost $8 each
    total_pant_cost = pant_cost_each * pants_bought

    # L4
    total_cost = total_shirt_cost + total_pant_cost

    # FA
    answer = total_cost
    return answer