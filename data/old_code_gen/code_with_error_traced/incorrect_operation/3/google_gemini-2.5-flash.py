def solve(
        book_pages: int = 120, # a 120-page book
        pages_read_yesterday: int = 12, # Yesterday, she was able to read 12 pages
        pages_read_today_multiplier: int = 2, # today, she read twice as many pages as yesterday
        fraction_remaining_to_read_tomorrow: float = 0.5 # half of the remaining pages tomorrow
    ):
    """Index: 3.
    Returns: the number of pages Julie should read tomorrow.
    """

    #: L1
    pages_read_today = pages_read_yesterday * pages_read_today_multiplier # eval: 24 = 12 * 2

    #: L2
    total_pages_read_so_far = pages_read_yesterday + pages_read_today # eval: 36 = 12 + 24

    #: L3
    remaining_pages = book_pages - total_pages_read_so_far # eval: 84 = 120 - 36

    #: L4
    pages_to_read_tomorrow = remaining_pages - fraction_remaining_to_read_tomorrow # eval: 83.5 = 84 - 0.5

    #: FA
    answer = pages_to_read_tomorrow
    return answer # eval: return 83.5
