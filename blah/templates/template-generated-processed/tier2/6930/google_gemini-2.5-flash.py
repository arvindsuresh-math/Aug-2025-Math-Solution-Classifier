def solve():
    """Index: 6930.
    Returns: the amount of money Josh has left.
    """
    # L1
    drink_cost = 1.75 # spent $1.75 on a drink
    additional_cost = 1.25 # spent another $1.25
    total_spent = drink_cost + additional_cost

    # L2
    initial_money = 9 # Josh has 9 dollars
    money_left = initial_money - total_spent

    # FA
    answer = money_left
    return answer