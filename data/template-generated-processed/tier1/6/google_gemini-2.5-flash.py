def solve():
    """Index: 6.
    Returns: the total number of pizza pieces Albert eats.
    """
    # L1
    num_large_pizzas = 2 # 2 large pizzas
    slices_per_large_pizza = 16 # 16 slices
    slices_from_large_pizzas = num_large_pizzas * slices_per_large_pizza

    # L2
    num_small_pizzas = 2 # 2 small pizzas
    slices_per_small_pizza = 8 # 8 slices
    slices_from_small_pizzas = num_small_pizzas * slices_per_small_pizza

    # L3
    total_slices = slices_from_large_pizzas + slices_from_small_pizzas

    # FA
    answer = total_slices
    return answer