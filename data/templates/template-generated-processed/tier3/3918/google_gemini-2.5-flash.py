def solve():
    """Index: 3918.
    Returns: the number of pages Jesse still has to read.
    """
    # L1
    chapter_1_pages = 10 # 10, 15, 27, 12, and 19 pages, respectively
    chapter_2_pages = 15 # 10, 15, 27, 12, and 19 pages, respectively
    chapter_3_pages = 27 # 10, 15, 27, 12, and 19 pages, respectively
    chapter_4_pages = 12 # 10, 15, 27, 12, and 19 pages, respectively
    chapter_5_pages = 19 # 10, 15, 27, 12, and 19 pages, respectively
    pages_read_so_far = chapter_1_pages + chapter_2_pages + chapter_3_pages + chapter_4_pages + chapter_5_pages

    # L2
    remaining_multiplier = 2 # twice as many pages
    pages_still_to_read = remaining_multiplier * pages_read_so_far

    # FA
    answer = pages_still_to_read
    return answer