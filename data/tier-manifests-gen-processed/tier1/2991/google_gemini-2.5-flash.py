def solve():
    """Index: 2991.
    Returns: the number of oranges Juan picked.
    """
    # L1
    del_oranges_per_day = 23 # Del picked 23
    del_picking_days = 2 # on each of 2 days
    del_total_oranges = del_oranges_per_day * del_picking_days

    # L2
    total_oranges_picked = 107 # A total of 107 oranges are picked
    juan_picked = total_oranges_picked - del_total_oranges

    # FA
    answer = juan_picked
    return answer