def solve():
    """Index: 2688.
    Returns: the total number of pens Roy has.
    """
    # L1
    blue_pens = 2 # Roy has 2 blue pens
    multiplier_for_black_pens = 2 # twice as many black
    black_pens = blue_pens * multiplier_for_black_pens

    # L2
    multiplier_for_red_base = 2 # twice as many red than black pens
    twice_black_pens = black_pens * multiplier_for_red_base

    # L3
    less_than_twice_red = 2 # 2 less than twice as many red
    red_pens = twice_black_pens - less_than_twice_red

    # L4
    total_pens = blue_pens + red_pens + black_pens

    # FA
    answer = total_pens
    return answer