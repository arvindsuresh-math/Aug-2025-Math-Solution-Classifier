def solve():
    """Index: 701.
    Returns: the cost of 5 slices of pizza.
    """
    # L1
    num_pizzas = 3 # Kim buys 3 pizzas
    slices_per_pizza = 12 # 12 slices each
    total_slices = num_pizzas * slices_per_pizza

    # L2
    total_cost = 72 # The pizza cost $72
    cost_per_slice = total_cost / total_slices

    # L3
    desired_slices = 5 # How much did 5 slices cost?
    cost_of_desired_slices = desired_slices * cost_per_slice

    # FA
    answer = cost_of_desired_slices
    return answer