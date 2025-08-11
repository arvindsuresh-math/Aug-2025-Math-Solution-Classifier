def solve():
    """Index: 6588.
    Returns: the number of pens left in the jar.
    """
    # L1
    initial_blue_pens = 9 # 9 blue pens
    removed_blue_pens = 4 # Four blue pens are removed
    remaining_blue_pens = initial_blue_pens - removed_blue_pens

    # L2
    initial_black_pens = 21 # 21 black pens
    removed_black_pens = 7 # seven black pens are removed
    remaining_black_pens = initial_black_pens - removed_black_pens

    # L3
    red_pens = 6 # 6 red pens
    total_remaining_pens = remaining_blue_pens + remaining_black_pens + red_pens

    # FA
    answer = total_remaining_pens
    return answer