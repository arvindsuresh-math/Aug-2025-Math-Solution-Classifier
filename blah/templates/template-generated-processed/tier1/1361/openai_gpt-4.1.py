def solve():
    """Index: 1361.
    Returns: the amount of money Annie had at first, in dollars.
    """
    # L1
    hamburger_price = 4 # hamburgers for $4 each
    hamburgers_bought = 8 # buys 8 hamburgers
    hamburger_total = hamburger_price * hamburgers_bought

    # L2
    milkshake_price = 5 # milkshakes for $5 each
    milkshakes_bought = 6 # buys 6 milkshakes
    milkshake_total = milkshake_price * milkshakes_bought

    # L3
    total_spent = hamburger_total + milkshake_total

    # L4
    money_left = 70 # She has $70 left
    initial_money = total_spent + money_left

    # FA
    answer = initial_money
    return answer