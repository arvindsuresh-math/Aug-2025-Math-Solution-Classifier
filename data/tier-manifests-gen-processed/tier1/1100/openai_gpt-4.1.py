def solve():
    """Index: 1100.
    Returns: the number of stickers Mary has remaining.
    """
    # L1
    stickers_per_page = 7 # 7 stickers each
    num_other_pages = 6 # 6 other pages
    stickers_other_pages = stickers_per_page * num_other_pages

    # L2
    large_stickers = 3 # 3 large stickers on the front page
    total_stickers_used = large_stickers + stickers_other_pages

    # L3
    initial_stickers = 89 # Mary had 89 stickers
    stickers_remaining = initial_stickers - total_stickers_used

    # FA
    answer = stickers_remaining
    return answer