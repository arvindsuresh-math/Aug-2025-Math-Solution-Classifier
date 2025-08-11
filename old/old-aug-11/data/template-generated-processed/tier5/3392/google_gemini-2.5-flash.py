def solve():
    """Index: 3392.
    Returns: the number of portraits Bethany saw.
    """
    # L3
    still_lifes_multiplier = 4 # 4 times more still lifes
    total_paintings = 80 # 80 paintings total
    coefficient_p = still_lifes_multiplier + 1

    # L4
    portraits = total_paintings / coefficient_p

    # FA
    answer = portraits
    return answer