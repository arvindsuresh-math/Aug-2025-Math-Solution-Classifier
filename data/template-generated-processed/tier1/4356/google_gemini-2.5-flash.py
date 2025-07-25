def solve():
    """Index: 4356.
    Returns: the total number of pizza slices.
    """
    # L1
    num_small_pizzas = 4 # 4 small pizzas
    num_medium_pizzas = 5 # 5 medium pizzas
    num_non_large_pizzas = num_small_pizzas + num_medium_pizzas

    # L2
    total_pizzas = 15 # total of 15 pizzas
    num_large_pizzas = total_pizzas - num_non_large_pizzas

    # L3
    slices_per_small_pizza = 6 # 6 slices
    total_small_slices = num_small_pizzas * slices_per_small_pizza

    # L4
    slices_per_medium_pizza = 8 # 8 slices
    total_medium_slices = num_medium_pizzas * slices_per_medium_pizza

    # L5
    slices_per_large_pizza = 12 # 12 slices
    total_large_slices = num_large_pizzas * slices_per_large_pizza

    # L6
    total_slices = total_small_slices + total_medium_slices + total_large_slices

    # FA
    answer = total_slices
    return answer