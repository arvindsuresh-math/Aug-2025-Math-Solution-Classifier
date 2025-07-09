def solve(
    total_pages: int = 120,  # Julie is reading a 120-page book
    pages_yesterday: int = 12  # Yesterday, she was able to read 12 pages
):
    """Index: 3.
    Returns: the number of pages Julie should read tomorrow.
    """

    #: L1
    pages_today = 23 # eval: 23 = 23

    #: L2
    pages_read_total = pages_yesterday + pages_today # eval: 35 = 12 + 23

    #: L3
    pages_remaining = total_pages - pages_read_total # eval: 85 = 120 - 35

    #: L4
    pages_tomorrow = pages_remaining / 2 # eval: 42.5 = 85 / 2

    #: FA
    answer = pages_tomorrow
    return answer # eval: return 42.5
