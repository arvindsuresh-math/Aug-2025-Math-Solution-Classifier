def solve(
        cost_toast_per_slice: int = 1, # A slice of toast costs £1
        cost_egg_per_egg: int = 3, # eggs cost £3 each
        dale_slices_toast: int = 2, # Dale had 2 slices of toast
        dale_num_eggs: int = 2, # and 2 eggs
        andrew_slices_toast: int = 1, # Andrew had 1 slice of toast
        andrew_num_eggs: int = 2 # and 2 eggs
    ):
    """Index: 75.
    Returns: the total cost of Dale and Andrew's breakfast.
    """

    #: L1
    cost_dale_toast = dale_slices_toast * cost_toast_per_slice

    #: L2
    cost_andrew_toast = andrew_slices_toast * cost_toast_per_slice

    #: L3
    cost_dale_eggs = dale_num_eggs * cost_egg_per_egg

    #: L4
    cost_andrew_eggs = andrew_num_eggs * cost_egg_per_egg

    #: L5
    total_breakfast_cost = cost_dale_toast * cost_andrew_toast + cost_dale_eggs + cost_andrew_eggs

    #: FA
    answer = total_breakfast_cost
    return answer