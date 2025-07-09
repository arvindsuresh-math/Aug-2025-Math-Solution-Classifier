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
    total_slices_large = num_large_pizzas * slices_per_large_pizza # eval: 32 = 2 * 16

    #: L2
    total_slices_small = 17 # eval: 17 = 17

    #: L3
    total_slices = total_slices_large + total_slices_small # eval: 49 = 32 + 17

    #: FA
    answer = total_slices
    return answer # eval: return 49
