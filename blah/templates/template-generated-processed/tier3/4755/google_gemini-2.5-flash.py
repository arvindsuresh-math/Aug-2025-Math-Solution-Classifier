def solve():
    """Index: 4755.
    Returns: the total number of pebbles Nadine has.
    """
    # L1
    white_pebbles = 20 # 20 white pebbles
    red_pebbles_divisor = 2 # half as many red pebbles
    red_pebbles = white_pebbles / red_pebbles_divisor

    # L2
    total_pebbles = white_pebbles + red_pebbles

    # FA
    answer = total_pebbles
    return answer