def solve():
    """Index: 722.
    Returns: the number of pages Coral must read in the third week to finish the book.
    """
    # L1
    total_pages = 600 # 600 pages long
    half_divisor = 2 # half of it
    pages_read_week1 = total_pages / half_divisor

    # L2
    pages_remaining_after_week1 = total_pages - pages_read_week1

    # L3
    percent_read_week2 = 0.30 # 30 percent of the remaining pages
    pages_read_week2 = pages_remaining_after_week1 * percent_read_week2

    # L4
    pages_remaining_after_week2 = pages_remaining_after_week1 - pages_read_week2

    # L5
    pages_to_read_week3 = pages_remaining_after_week2

    # FA
    answer = pages_to_read_week3
    return answer