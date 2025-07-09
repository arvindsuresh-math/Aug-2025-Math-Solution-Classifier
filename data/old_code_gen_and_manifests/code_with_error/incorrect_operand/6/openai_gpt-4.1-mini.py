def solve(
    num_large_pizzas: int = 2,  # Albert buys 2 large pizzas
    num_small_pizzas: int = 2,  # Albert buys 2 small pizzas
    slices_per_large_pizza: int = 16,  # A large pizza has 16 slices
    slices_per_small_pizza: int = 8  # A small pizza has 8 slices
):
    """Index: 6.
    Returns: the total number of pizza slices Albert eats in one day.
    """

    #: L1
    total_slices_large = num_large_pizzas * num_small_pizzas

    #: L2
    total_slices_small = num_small_pizzas * slices_per_small_pizza

    #: L3
    total_slices = total_slices_large + total_slices_small

    #: FA
    answer = total_slices
    return answer