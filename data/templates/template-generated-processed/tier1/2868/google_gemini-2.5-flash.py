def solve():
    """Index: 2868.
    Returns: the total number of pens in Maria's desk drawer.
    """
    # L1
    red_pens = 8 # 8 red pens
    more_black_than_red = 10 # 10 more black pens than red pens
    black_pens = red_pens + more_black_than_red

    # L2
    more_blue_than_red = 7 # 7 more blue pens than red pens
    blue_pens = red_pens + more_blue_than_red

    # L3
    total_pens = red_pens + black_pens + blue_pens

    # FA
    answer = total_pens
    return answer