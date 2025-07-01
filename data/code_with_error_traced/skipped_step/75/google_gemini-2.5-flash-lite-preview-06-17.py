def solve(
    toast_cost: int = 1, # A slice of toast costs £1
    egg_cost: int = 3, # eggs cost £3 each
    dale_toast: int = 2, # Dale had 2 slices of toast
    dale_eggs: int = 2, # and 2 eggs
    andrew_toast: int = 1, # Andrew had 1 slice of toast
    andrew_eggs: int = 2 # and 2 eggs
):
    """Index: 75.
    Returns: the total cost of their breakfast.
    """

    #: L1
    dale_toast_cost = dale_toast * toast_cost # eval: 2 = 2 * 1

    #: L2
    andrew_toast_cost = andrew_toast * toast_cost # eval: 1 = 1 * 1

    #: L3
    dale_eggs_cost = dale_eggs * egg_cost # eval: 6 = 2 * 3

    #: L4

    #: L5
    total_cost = dale_toast_cost + andrew_toast_cost + dale_eggs_cost + dale_toast # eval: 11 = 2 + 1 + 6 + 2

    #: FA
    answer = total_cost
    return answer # eval: return 11
