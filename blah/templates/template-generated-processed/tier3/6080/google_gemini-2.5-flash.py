def solve():
    """Index: 6080.
    Returns: the number of pizza slices left over.
    """
    # L1
    slices_per_pizza = 12 # each pizza is cut into 12 slices
    bob_denominator = 2 # Bob ate half of a pizza
    bob_slices = slices_per_pizza / bob_denominator

    # L2
    tom_denominator = 3 # Tom ate one-third of a pizza
    tom_slices = slices_per_pizza / tom_denominator

    # L3
    sally_denominator = 6 # only ate one-sixth of a pizza
    sally_slices = slices_per_pizza / sally_denominator

    # L4
    jerry_denominator = 4 # Jerry ate a quarter of a pizza
    jerry_slices = slices_per_pizza / jerry_denominator

    # L5
    total_eaten_slices = bob_slices + tom_slices + sally_slices + jerry_slices

    # L6
    num_pizzas = 2 # share 2 pizzas
    left_over_slices = slices_per_pizza * num_pizzas - total_eaten_slices

    # FA
    answer = left_over_slices
    return answer