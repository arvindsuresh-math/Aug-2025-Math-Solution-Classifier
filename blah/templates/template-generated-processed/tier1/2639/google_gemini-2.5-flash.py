def solve():
    """Index: 2639.
    Returns: the amount of money Mitzi has left.
    """
    # L1
    ticket_cost = 30 # spent $30 on a ticket
    food_cost = 13 # spent $13 on food
    tshirt_cost = 23 # spent $23 on a T-shirt
    total_spent = ticket_cost + food_cost + tshirt_cost

    # L2
    initial_money = 75 # brought $75 to the amusement park
    money_left = initial_money - total_spent

    # FA
    answer = money_left
    return answer