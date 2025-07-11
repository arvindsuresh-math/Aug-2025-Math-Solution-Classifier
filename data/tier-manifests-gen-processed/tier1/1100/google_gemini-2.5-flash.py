def solve():
    """Index: 1100.
    Returns: the number of stickers Mary has remaining.
    """
    # L1
    stickers_per_other_page = 7 # 7 stickers each
    num_other_pages = 6 # 6 other pages
    stickers_on_other_pages = stickers_per_other_page * num_other_pages

    # L2
    large_stickers_front_page = 3 # 3 large stickers
    total_stickers_added = large_stickers_front_page + stickers_on_other_pages

    # L3
    initial_stickers = 89 # Mary had 89 stickers
    remaining_stickers = initial_stickers - total_stickers_added

    # FA
    answer = remaining_stickers
    return answer