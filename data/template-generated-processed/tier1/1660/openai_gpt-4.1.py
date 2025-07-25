def solve():
    """Index: 1660.
    Returns: the number of green papayas left on the tree.
    """
    # L1
    friday_turned_yellow = 2 # two of the fruits turned yellow
    sunday_turned_yellow = friday_turned_yellow * 2

    # L2
    total_turned_yellow = friday_turned_yellow + sunday_turned_yellow

    # L3
    initial_green_papayas = 14 # There are 14 green papayas on the papaya tree
    green_papayas_left = initial_green_papayas - total_turned_yellow

    # FA
    answer = green_papayas_left
    return answer