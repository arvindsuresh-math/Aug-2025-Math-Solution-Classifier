def solve():
    """Index: 1891.
    Returns: the number of stickers Xia had at the beginning.
    """
    # L1
    sheets_left = 5 # five sheets of stickers left
    stickers_per_sheet = 10 # each sheet had ten stickers on it
    stickers_left = sheets_left * stickers_per_sheet

    # L2
    stickers_shared = 100 # sharing 100 stickers with her friends
    total_stickers = stickers_shared + stickers_left

    # FA
    answer = total_stickers
    return answer