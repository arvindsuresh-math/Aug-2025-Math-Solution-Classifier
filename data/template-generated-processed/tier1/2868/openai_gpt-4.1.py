def solve():
    """Index: 2868.
    Returns: the total number of pens Maria has in all.
    """
    # L1
    red_pens = 8 # 8 red pens in Maria's desk drawer
    black_more_than_red = 10 # 10 more black pens than red pens
    black_pens = red_pens + black_more_than_red

    # L2
    blue_more_than_red = 7 # 7 more blue pens than red pens
    blue_pens = red_pens + blue_more_than_red

    # L3
    total_pens = red_pens + black_pens + blue_pens

    # FA
    answer = total_pens
    return answer