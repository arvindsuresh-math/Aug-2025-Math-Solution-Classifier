def solve():
    """Index: 1891.
    Returns: the number of stickers Xia had at the beginning.
    """
    # L1
    sheets_left = 5 # five sheets of stickers left
    stickers_per_sheet = 10 # ten stickers on it
    stickers_remaining = sheets_left * stickers_per_sheet

    # L2
    stickers_shared = 100 # sharing 100 stickers
    initial_stickers = stickers_shared + stickers_remaining

    # FA
    answer = initial_stickers
    return answer