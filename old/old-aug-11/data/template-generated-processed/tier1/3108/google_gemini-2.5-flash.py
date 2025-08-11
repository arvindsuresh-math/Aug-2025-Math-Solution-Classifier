def solve():
    """Index: 3108.
    Returns: the amount of money Annie has left.
    """
    # L1
    hamburger_price = 4 # sells hamburgers for $4 each
    num_hamburgers = 8 # buys 8 hamburgers
    cost_hamburgers = hamburger_price * num_hamburgers

    # L2
    milkshake_price = 3 # sells milkshakes for $3 each
    num_milkshakes = 6 # buys 6 milkshakes
    cost_milkshakes = milkshake_price * num_milkshakes

    # L3
    total_spent = cost_hamburgers + cost_milkshakes

    # L4
    initial_money = 120 # Annie has $120
    money_left = initial_money - total_spent

    # FA
    answer = money_left
    return answer