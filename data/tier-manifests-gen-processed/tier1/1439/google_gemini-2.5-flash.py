def solve():
    """Index: 1439.
    Returns: the amount of change Gemma got back.
    """
    # L1
    num_pizzas = 4 # four pizzas
    cost_per_pizza = 10 # $10 each
    cost_pizzas = num_pizzas * cost_per_pizza

    # L2
    tip_amount = 5 # $5 tip
    total_cost = cost_pizzas + tip_amount

    # L3
    bill_given = 50 # one fifty-dollar bill
    change_back = bill_given - total_cost

    # FA
    answer = change_back
    return answer