def solve():
    """Index: 1361.
    Returns: the amount of money Annie had at first.
    """
    # L1
    hamburger_price = 4 # hamburgers for $4 each
    num_hamburgers = 8 # buys 8 hamburgers
    cost_hamburgers = hamburger_price * num_hamburgers

    # L2
    milkshake_price = 5 # milkshakes for $5 each
    num_milkshakes = 6 # buys 6 milkshakes
    cost_milkshakes = milkshake_price * num_milkshakes

    # L3
    total_spent = cost_hamburgers + cost_milkshakes

    # L4
    money_left = 70 # She has $70 left
    initial_money = total_spent + money_left

    # FA
    answer = initial_money
    return answer