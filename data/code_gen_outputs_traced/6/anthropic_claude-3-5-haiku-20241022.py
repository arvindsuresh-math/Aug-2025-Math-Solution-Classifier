def solve(
    num_large_pizzas: int = 2,  # Albert buys 2 large pizzas
    num_small_pizzas: int = 2,  # and 2 small pizzas
    slices_large_pizza: int = 16,  # A large pizza has 16 slices
    slices_small_pizza: int = 8  # a small pizza has 8 slices
):
    """Index: 6.
    Returns: the total number of pizza slices Albert eats in one day.
    """
    #: L1
    large_pizza_slices = num_large_pizzas * slices_large_pizza # eval: 32 = 2 * 16
    #: L2
    small_pizza_slices = num_small_pizzas * slices_small_pizza # eval: 16 = 2 * 8
    answer = large_pizza_slices + small_pizza_slices  # FINAL ANSWER # eval: 48 = 32 + 16  # FINAL ANSWER
    return answer # eval: return 48