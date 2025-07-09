def solve(
    total_pages: int = 120,  # Julie is reading a 120-page book
    pages_yesterday: int = 12  # Yesterday, she was able to read 12 pages
):
    """Index: 3.
    Returns: the number of pages Julie should read tomorrow.
    """
    #: L1
    pages_today = pages_yesterday * 2

    #: L2
    pages_read_total = pages_yesterday + pages_today

    #: L3
    pages_remaining = total_pages - pages_read_total

    #: L4
    pages_tomorrow = pages_remaining / 2

    answer = pages_tomorrow  # FINAL ANSWER
    return answer