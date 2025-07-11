def solve():
    """Index: 2664.
    Returns: the number of pizza slices left after guests eat some.
    """
    # L1
    num_pizzas = 4 # 4 pizzas
    slices_per_pizza = 12 # 12 slices each
    total_slices = num_pizzas * slices_per_pizza

    # L2
    slices_eaten = 39 # eat 39 slices
    slices_left = total_slices - slices_eaten

    # FA
    answer = slices_left
    return answer