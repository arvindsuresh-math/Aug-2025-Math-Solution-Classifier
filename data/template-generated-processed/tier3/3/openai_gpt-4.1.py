def solve():
    """Index: 3.
    Returns: the number of pages Julie should read tomorrow.
    """
    # L1
    pages_read_yesterday = 12 # she was able to read 12 pages
    pages_read_today = pages_read_yesterday * 2 # twice as many pages as yesterday

    # L2
    total_pages_read = pages_read_yesterday + pages_read_today

    # L3
    total_pages = 120 # Julie is reading a 120-page book
    pages_left = total_pages - total_pages_read

    # L4
    tomorrow_fraction_denominator = 2 # read half of the remaining pages
    pages_to_read_tomorrow = pages_left / tomorrow_fraction_denominator

    # FA
    answer = pages_to_read_tomorrow
    return answer