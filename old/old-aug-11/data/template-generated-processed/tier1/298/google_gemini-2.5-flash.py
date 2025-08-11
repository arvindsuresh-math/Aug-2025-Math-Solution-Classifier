def solve():
    """Index: 298.
    Returns: the initial number of sweets on the table.
    """
    # L1
    paul_took_remaining = 7 # took the remaining 7 sweets
    jack_took_more = 4 # 4 more candies
    half_total_candies = paul_took_remaining + jack_took_more

    # L2
    multiplier_for_total = 2 # WK
    initial_sweets = half_total_candies * multiplier_for_total

    # FA
    answer = initial_sweets
    return answer