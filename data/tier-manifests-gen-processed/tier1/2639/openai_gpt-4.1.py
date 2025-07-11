def solve():
    """Index: 2639.
    Returns: the amount of money Mitzi has left after her purchases.
    """
    # L1
    ticket_cost = 30 # $30 on a ticket
    food_cost = 13 # $13 on food
    tshirt_cost = 23 # $23 on a T-shirt
    total_spent = ticket_cost + food_cost + tshirt_cost

    # L2
    initial_money = 75 # Mitzi brought $75
    money_left = initial_money - total_spent

    # FA
    answer = money_left
    return answer