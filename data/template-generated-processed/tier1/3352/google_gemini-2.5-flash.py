def solve():
    """Index: 3352.
    Returns: the total number of pens in Sam's collection.
    """
    # L1
    num_pencils = 8 # eight pencils
    blue_pens_multiplier_pencils = 2 # twice as many blue pens as pencils
    num_blue_pens = num_pencils * blue_pens_multiplier_pencils

    # L2
    black_pens_more_than_blue = 10 # ten more black pens than blue pens
    num_black_pens = num_blue_pens + black_pens_more_than_blue

    # L3
    red_pens_fewer_than_pencils = 2 # two fewer red pens than pencils
    num_red_pens = num_pencils - red_pens_fewer_than_pencils

    # L4
    total_pens = num_blue_pens + num_black_pens + num_red_pens

    # FA
    answer = total_pens
    return answer