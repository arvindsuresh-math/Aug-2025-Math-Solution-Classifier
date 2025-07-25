def solve(
    cost_toast: int = 1, # A slice of toast costs £1
    cost_eggs: int = 3, # eggs cost £3 each
    dale_toast: int = 2, # Dale had 2 slices of toast
    dale_eggs: int = 2, # and 2 eggs
    andrew_toast: int = 1, # Andrew had 1 slice of toast
    andrew_eggs: int = 2 # and 2 eggs
):
    """Index: 75.
    Returns: the total cost of their breakfast.
    """
    #: L1
    dale_toast_cost = dale_toast * cost_toast

    #: L2
    andrew_toast_cost = andrew_toast * cost_toast

    #: L3
    dale_eggs_cost = dale_eggs * cost_eggs

    #: L4
    andrew_eggs_cost = andrew_eggs * cost_eggs

    #: L5
    total_cost = dale_toast_cost + andrew_toast_cost + dale_eggs_cost + andrew_eggs_cost

    answer = total_cost # FINAL ANSWER
    return answer