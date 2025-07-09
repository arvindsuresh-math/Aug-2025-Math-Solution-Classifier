def solve(
    cost_toast_slice: int = 1, # A slice of toast costs £1
    cost_egg: int = 3, # eggs cost £3 each
    dale_toast_slices: int = 2, # Dale had 2 slices of toast
    dale_eggs: int = 2, # and 2 eggs
    andrew_toast_slices: int = 1, # Andrew had 1 slice of toast
    andrew_eggs: int = 2 # and 2 eggs
):
    """Index: 75.
    Returns: the total cost of their breakfast.
    """

    #: L1
    cost_dale_toast = dale_toast_slices * cost_toast_slice # eval: 2 = 2 * 1

    #: L2
    cost_andrew_toast = andrew_toast_slices * cost_toast_slice # eval: 1 = 1 * 1

    #: L3
    cost_dale_eggs = dale_eggs * cost_egg # eval: 6 = 2 * 3

    #: L4
    cost_andrew_eggs = 5 # eval: 5 = 5

    #: L5
    total_cost = cost_dale_toast + cost_andrew_toast + cost_dale_eggs + cost_andrew_eggs # eval: 14 = 2 + 1 + 6 + 5

    #: FA
    answer = total_cost
    return answer # eval: return 14
