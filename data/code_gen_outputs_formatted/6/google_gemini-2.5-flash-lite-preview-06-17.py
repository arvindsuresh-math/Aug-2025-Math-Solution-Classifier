def solve(
    num_large_pizzas: int = 2, # Albert buys 2 large pizzas
    num_small_pizzas: int = 2, # and 2 small pizzas
    slices_large_pizza: int = 16, # A large pizza has 16 slices
    slices_small_pizza: int = 8 # a small pizza has 8 slices
):
    """Index: 6.
    Returns: the total number of pizza slices Albert eats in a day.
    """

    #: L1
    slices_from_large_pizzas = num_large_pizzas * slices_large_pizza

    #: L2
    slices_from_small_pizzas = num_small_pizzas * slices_small_pizza

    #: L3
    total_slices = slices_from_large_pizzas + slices_from_small_pizzas

    #: FA
    answer = total_slices
    return answer