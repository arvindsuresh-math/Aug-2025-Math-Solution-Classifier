def solve():
    """Index: 1439.
    Returns: the amount of change Gemma gets back from a $50 bill after paying for pizzas and tip.
    """
    # L1
    num_pizzas = 4 # four pizzas
    price_per_pizza = 10 # $10 each
    cost_pizzas = num_pizzas * price_per_pizza

    # L2
    tip = 5 # $5 tip
    total_cost = cost_pizzas + tip

    # L3
    bill_given = 50 # one fifty-dollar bill
    change = bill_given - total_cost

    # FA
    answer = change
    return answer