def solve():
    """Index: 611.
    Returns: the number of pepperoni slices on the slice Lard gives Jelly.
    """
    # L1
    initial_pizza_halves = 1 # WK
    first_cut_factor = 2 # cuts it in half
    slices_after_first_cut = initial_pizza_halves * first_cut_factor

    # L2
    second_cut_factor = 2 # cuts these halves in half
    total_pizza_slices = slices_after_first_cut * second_cut_factor

    # L3
    initial_pepperoni_slices = 40 # pizza started with 40 evenly spread slices of pepperoni
    pepperoni_per_slice = initial_pepperoni_slices / total_pizza_slices

    # L4
    fallen_pepperoni = 1 # 1 of them falls off the slice
    pepperoni_on_jellys_slice = pepperoni_per_slice - fallen_pepperoni

    # FA
    answer = pepperoni_on_jellys_slice
    return answer