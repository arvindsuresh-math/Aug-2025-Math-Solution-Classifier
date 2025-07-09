def solve(
    total_pages: int = 120, # Julie is reading a 120-page book.
    pages_read_yesterday: int = 12, # Yesterday, she was able to read 12 pages
    pages_read_today_multiplier: int = 2, # and today, she read twice as many pages as yesterday.
    fraction_remaining_to_read_tomorrow: float = 0.5 # she wants to read half of the remaining pages tomorrow
):
    """Index: 3.
    Returns: the number of pages Julie should read tomorrow.
    """
    #: L1
    pages_read_today = pages_read_yesterday * pages_read_today_multiplier

    #: L2
    total_pages_read = pages_read_yesterday + pages_read_today

    #: L3
    remaining_pages = total_pages - total_pages_read

    #: L4
    pages_to_read_tomorrow = remaining_pages * fraction_remaining_to_read_tomorrow

    answer = pages_to_read_tomorrow # FINAL ANSWER
    return answer