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
    pages_read_today = multiplier_today * multiplier_today # eval: 4 = 2 * 2

    #: L2
    total_pages_read_so_far = pages_read_yesterday + pages_read_today # eval: 16 = 12 + 4

    #: L3
    remaining_pages = total_pages - total_pages_read_so_far # eval: 104 = 120 - 16

    #: L4
    pages_to_read_tomorrow = remaining_pages * fraction_tomorrow # eval: 52.0 = 104 * 0.5

    #: FA
    answer = pages_to_read_tomorrow
    return answer # eval: return 52.0
