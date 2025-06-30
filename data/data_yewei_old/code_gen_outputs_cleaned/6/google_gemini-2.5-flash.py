def solve_6():
    """
    Calculates the total number of pizza slices Albert eats in one day.

    Albert buys 2 large pizzas (16 slices each) and 2 small pizzas (8 slices each).
    """
    num_large_pizzas = 2
    slices_per_large_pizza = 16
    num_small_pizzas = 2
    slices_per_small_pizza = 8

    # Calculate total slices from large pizzas
    total_slices_large = num_large_pizzas * slices_per_large_pizza

    # Calculate total slices from small pizzas
    total_slices_small = num_small_pizzas * slices_per_small_pizza

    # Calculate the grand total of slices
    total_slices_eaten = total_slices_large + total_slices_small

    return total_slices_eaten