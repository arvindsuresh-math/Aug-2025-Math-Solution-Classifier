def solve():
    """Index: 611.
    Returns: the number of pepperoni slices on the slice Lard gives Jelly after 1 falls off.
    """
    # L1
    initial_slices = 1 # whole, uncut pizza
    first_cut_multiplier = 2 # cuts it in half
    slices_after_first_cut = initial_slices * first_cut_multiplier

    # L2
    second_cut_multiplier = 2 # cuts these halves in half
    total_pizza_slices = slices_after_first_cut * second_cut_multiplier

    # L3
    total_pepperoni = 40 # 40 evenly spread slices of pepperoni
    pepperoni_per_slice = total_pepperoni / total_pizza_slices

    # L4
    fallen_pepperoni = 1 # 1 of them falls off
    pepperoni_on_jelly_slice = pepperoni_per_slice - fallen_pepperoni

    # FA
    answer = pepperoni_on_jelly_slice
    return answer