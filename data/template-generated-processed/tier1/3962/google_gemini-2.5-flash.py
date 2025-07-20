def solve():
    """Index: 3962.
    Returns: the amount of change Lucas brings home.
    """
    # L1
    num_avocados = 3 # buy 3 avocados
    cost_per_avocado = 2 # cost $2 each
    total_avocado_cost = num_avocados * cost_per_avocado

    # L2
    initial_money = 20 # with $20
    change = initial_money - total_avocado_cost

    # FA
    answer = change
    return answer