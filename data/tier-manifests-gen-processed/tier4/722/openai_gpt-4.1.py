def solve():
    """Index: 722.
    Returns: the number of pages Coral must read in the third week to finish the book.
    """
    # L1
    total_pages = 600 # 600 pages long
    week1_divisor = 2 # reads half of it in the first week
    week1_pages = total_pages / week1_divisor

    # L2
    after_week1 = total_pages - week1_pages

    # L3
    week2_percent = 0.30 # 30 percent of the remaining pages the second week
    week2_pages = after_week1 * week2_percent

    # L4
    after_week2 = after_week1 - week2_pages

    # L5
    week3_pages = after_week2

    # FA
    answer = week3_pages
    return answer