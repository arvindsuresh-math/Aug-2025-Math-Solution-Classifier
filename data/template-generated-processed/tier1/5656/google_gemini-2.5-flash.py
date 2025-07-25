def solve():
    """Index: 5656.
    Returns: the total number of pages in Siena's bookmarks library at the end of March.
    """
    # L1
    pages_per_day = 30 # bookmarks 30 website pages from the research she does on her browser every day
    days_in_march = 31 # at the end of March, with 31 days
    pages_bookmarked_march = pages_per_day * days_in_march

    # L2
    current_pages = 400 # has 400 bookmarked pages on her bookmarks library now
    total_pages_end_march = pages_bookmarked_march + current_pages

    # FA
    answer = total_pages_end_march
    return answer