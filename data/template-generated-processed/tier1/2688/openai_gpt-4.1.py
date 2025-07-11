def solve():
    """Index: 2688.
    Returns: the total number of pens Roy has in all.
    """
    # L1
    blue_pens = 2 # Roy has 2 blue pens
    black_multiplier = 2 # twice as many black
    black_pens = blue_pens * black_multiplier

    # L2
    red_multiplier = 2 # twice as many red than black pens
    twice_black = black_pens * red_multiplier

    # L3
    red_less = 2 # 2 less than twice as many red than black pens
    red_pens = twice_black - red_less

    # L4
    total_pens = blue_pens + red_pens + black_pens

    # FA
    answer = total_pens
    return answer