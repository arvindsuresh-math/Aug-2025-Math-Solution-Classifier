def solve(
    total_pages: int = 120, # reading a 120-page book
    pages_read_yesterday: int = 12, # Yesterday, she was able to read 12 pages
    multiplier_today: int = 2, # today, she read twice as many pages as yesterday
    fraction_tomorrow: float = 1/2 # read half of the remaining pages tomorrow
):
    """Index: 3.
    Returns: the number of pages Julie should read tomorrow.
    """

    #: L1
    pages_read_today = pages_read_yesterday * multiplier_today

    #: L2
    total_pages_read_so_far = pages_read_yesterday + pages_read_today

    #: L3
    remaining_pages = total_pages + total_pages_read_so_far

    #: L4
    pages_to_read_tomorrow = remaining_pages * fraction_tomorrow

    #: FA
    answer = pages_to_read_tomorrow
    return answer