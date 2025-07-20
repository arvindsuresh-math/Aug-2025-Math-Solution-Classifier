def solve():
    """Index: 4226.
    Returns: the number of slices remaining after Mary eats some.
    """
    # L1
    slices_per_pizza = 8 # 8 slices in a large pizza
    num_pizzas = 2 # 2 large pizzas
    total_slices = slices_per_pizza * num_pizzas

    # L2
    mary_eats_slices = 7 # eats 7 slices
    remaining_slices = total_slices - mary_eats_slices

    # FA
    answer = remaining_slices
    return answer