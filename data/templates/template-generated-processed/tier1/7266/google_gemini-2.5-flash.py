def solve():
    """Index: 7266.
    Returns: the number of pieces of candy the peanut butter jar had.
    """
    # L1
    banana_candy_pieces = 43 # banana jar had 43
    grape_more_than_banana = 5 # 5 more pieces of candy
    grape_candy_pieces = banana_candy_pieces + grape_more_than_banana

    # L2
    pb_times_grape = 4 # 4 times as much candy
    peanut_butter_candy_pieces = grape_candy_pieces * pb_times_grape

    # FA
    answer = peanut_butter_candy_pieces
    return answer