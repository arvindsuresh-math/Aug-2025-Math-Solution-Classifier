def solve():
    """Index: 1782.
    Returns: the total cost of one pizza and three burgers.
    """
    # L1
    burger_cost = 9 # a burger costs $9
    pizza_multiplier = 2 # pizza twice as much
    pizza_cost = burger_cost * pizza_multiplier

    # L2
    num_burgers = 3 # three burgers
    burgers_total = burger_cost * num_burgers

    # L3
    total_cost = pizza_cost + burgers_total

    # FA
    answer = total_cost
    return answer