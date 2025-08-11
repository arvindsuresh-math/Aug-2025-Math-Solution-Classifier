def solve():
    """Index: 1203.
    Returns: the initial amount of money Josh had.
    """
    # L1
    drink_cost = 1.75 # spent $1.75 on a drink
    additional_spent = 1.25 # spent another $1.25
    total_spent = drink_cost + additional_spent

    # L2
    money_left = 6 # had $6 left
    initial_money = money_left + total_spent

    # FA
    answer = initial_money
    return answer