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
    cost_dale_toast = dale_slices_toast * cost_toast_per_slice # eval: 2 = 2 * 1

    #: L2
    cost_andrew_toast = andrew_slices_toast * cost_toast_per_slice # eval: 1 = 1 * 1

    #: L3
    cost_dale_eggs = 7 # eval: 7 = 7

    #: L4
    cost_andrew_eggs = andrew_num_eggs * cost_egg_per_egg # eval: 6 = 2 * 3

    #: L5
    total_breakfast_cost = cost_dale_toast + cost_andrew_toast + cost_dale_eggs + cost_andrew_eggs # eval: 16 = 2 + 1 + 7 + 6

    #: FA
    answer = total_breakfast_cost
    return answer # eval: return 16
