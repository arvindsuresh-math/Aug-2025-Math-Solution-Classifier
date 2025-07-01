def solve(
        total_pages: int = 120,  # Julie is reading a 120-page book
        pages_read_yesterday: int = 12,  # Yesterday, she was able to read 12 pages
        pages_multiplier: int = 2  # today, she read twice as many pages as yesterday
    ):
    """Index: 3.
    Returns: the number of pages Julie should read tomorrow.
    """

    #: L1
    pages_read_today = pages_read_yesterday * pages_multiplier # eval: 24 = 12 * 2

    #: L2
    total_pages_read = pages_read_yesterday - pages_read_today # eval: -12 = 12 - 24

    #: L3
    remaining_pages = total_pages - total_pages_read # eval: 132 = 120 - -12

    #: L4
    pages_to_read_tomorrow = remaining_pages / 2 # eval: 66.0 = 132 / 2

    #: FA
    answer = pages_to_read_tomorrow
    return answer # eval: return 66.0
