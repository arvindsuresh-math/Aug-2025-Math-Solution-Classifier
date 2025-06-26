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
    total_large_slices = num_large_pizzas * slices_per_large_pizza

    #: L2
    total_small_slices = num_small_pizzas * slices_per_small_pizza

    #: L3
    total_slices_eaten = total_large_slices + total_small_slices

    answer = total_slices_eaten  # FINAL ANSWER
    return answer