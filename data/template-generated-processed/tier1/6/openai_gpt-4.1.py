def solve():
    """Index: 6.
    Returns: the total number of pizza slices Albert eats in one day.
    """
    # L1
    num_large_pizzas = 2 # 2 large pizzas
    slices_per_large = 16 # A large pizza has 16 slices
    large_total = num_large_pizzas * slices_per_large

    # L2
    num_small_pizzas = 2 # 2 small pizzas
    slices_per_small = 8 # a small pizza has 8 slices
    small_total = num_small_pizzas * slices_per_small

    # L3
    total_slices = large_total + small_total

    # FA
    answer = total_slices
    return answer