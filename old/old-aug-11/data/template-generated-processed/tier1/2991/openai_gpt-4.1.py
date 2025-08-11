def solve():
    """Index: 2991.
    Returns: the number of oranges Juan picked.
    """
    # L1
    del_per_day = 23 # Del picked 23 on each of 2 days
    del_days = 2 # each of 2 days
    del_total = del_per_day * del_days

    # L2
    total_oranges = 107 # A total of 107 oranges are picked
    juan_total = total_oranges - del_total

    # FA
    answer = juan_total
    return answer