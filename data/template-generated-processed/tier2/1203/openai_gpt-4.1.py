def solve():
    """Index: 1203.
    Returns: the amount of money Josh had at first, in dollars.
    """
    # L1
    drink_cost = 1.75 # spent $1.75 on a drink
    other_spending = 1.25 # spent another $1.25
    total_spent = drink_cost + other_spending

    # L2
    money_left = 6 # he had $6 left
    initial_money = money_left + total_spent

    # FA
    answer = initial_money
    return answer