def solve():
    """Index: 3.
    Returns: the number of pages Julie should read tomorrow.
    """
    # L1
    pages_read_yesterday = 12 # Yesterday, she was able to read 12 pages
    twice_factor = 2 # twice as many pages
    pages_read_today = pages_read_yesterday * twice_factor

    # L2
    total_pages_read_so_far = pages_read_yesterday + pages_read_today

    # L3
    total_book_pages = 120 # Julie is reading a 120-page book
    remaining_pages = total_book_pages - total_pages_read_so_far

    # L4
    half_factor = 2 # half of the remaining pages
    pages_to_read_tomorrow = remaining_pages / half_factor

    # FA
    answer = pages_to_read_tomorrow
    return answer