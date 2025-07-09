def solve(
    total_pages: int = 120,  # Julie is reading a 120-page book
    pages_yesterday: int = 12  # Yesterday, she was able to read 12 pages
):
    """Index: 3.
    Returns: the number of pages Julie should read tomorrow.
    """

    #: L1
    pages_today = total_pages * 2 # eval: 240 = 120 * 2

    #: L2
    pages_read_total = pages_yesterday + pages_today # eval: 252 = 12 + 240

    #: L3
    pages_remaining = total_pages - pages_read_total # eval: -132 = 120 - 252

    #: L4
    pages_tomorrow = pages_remaining / 2 # eval: -66.0 = -132 / 2

    #: FA
    answer = pages_tomorrow
    return answer # eval: return -66.0
