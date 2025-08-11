def solve():
    """Index: 6692.
    Returns: the total number of oranges picked.
    """
    # L2
    thrice_multiplier = 3 # thrice as much
    oranges_monday = 100 # picks 100 oranges
    oranges_tuesday = thrice_multiplier * oranges_monday

    # L3
    total_after_tuesday = oranges_tuesday + oranges_monday

    # L4
    oranges_wednesday = 70 # pick 70 oranges
    total_oranges = total_after_tuesday + oranges_wednesday

    # FA
    answer = total_oranges
    return answer