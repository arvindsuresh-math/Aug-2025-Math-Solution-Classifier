def solve():
    """Index: 6070.
    Returns: the cost of each piece of pizza in dollars.
    """
    # L1
    total_cost = 80 # $80
    num_pizzas = 4 # four pizzas
    cost_per_pizza = total_cost / num_pizzas

    # L2
    pieces_per_pizza = 5 # 5 pieces
    cost_per_piece = cost_per_pizza / pieces_per_pizza

    # FA
    answer = cost_per_piece
    return answer