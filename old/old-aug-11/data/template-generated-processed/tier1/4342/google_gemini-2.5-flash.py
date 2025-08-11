def solve():
    """Index: 4342.
    Returns: the total number of stickers after losing one page.
    """
    # L1
    total_pages = 12 # 12 pages of stickers
    lost_pages = 1 # lose one of the pages
    remaining_pages = total_pages - lost_pages

    # L2
    stickers_per_page = 20 # 20 stickers on a page
    total_stickers = remaining_pages * stickers_per_page

    # FA
    answer = total_stickers
    return answer