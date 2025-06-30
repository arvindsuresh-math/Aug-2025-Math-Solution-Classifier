def solve(
    toast_price: float = 1,  # A slice of toast costs £1
    egg_price: float = 3,    # eggs cost £3 each
    dale_toast_slices: int = 2,  # Dale had 2 slices of toast
    dale_eggs: int = 2,  # Dale had 2 eggs
    andrew_toast_slices: int = 1,  # Andrew had 1 slice of toast
    andrew_eggs: int = 2  # Andrew had 2 eggs
):
    """Index: 75.
    Returns: the total cost of Dale and Andrew's breakfast."""

    #: L1
    dale_toast_cost = dale_toast_slices * toast_price

    #: L2
    andrew_toast_cost = andrew_toast_slices * toast_price

    #: L3
    dale_eggs_cost = dale_eggs * egg_price

    #: L4
    andrew_eggs_cost = andrew_eggs * egg_price

    #: L5
    total_breakfast_cost = dale_toast_cost - andrew_toast_cost + dale_eggs_cost + andrew_eggs_cost

    #: FA
    answer = total_breakfast_cost
    return answer