def solve():
    """Index: 3371.
    Returns: the number of pages in the first chapter.
    """
    # L3
    increment_per_chapter = 3 # Each chapter has three pages more than the previous one
    sum_of_increments_chap3 = increment_per_chapter + increment_per_chapter

    # L4
    sum_of_increments_chap4 = sum_of_increments_chap3 + increment_per_chapter

    # L5
    sum_of_increments_chap5 = sum_of_increments_chap4 + increment_per_chapter

    # L6
    num_chapters = 5 # five-chapter book
    total_pages_book = 95 # 95 pages
    total_offset_sum = increment_per_chapter + sum_of_increments_chap3 + sum_of_increments_chap4 + sum_of_increments_chap5

    # L7
    pages_for_P_terms = total_pages_book - total_offset_sum

    # L8
    first_chapter_pages = pages_for_P_terms / num_chapters

    # FA
    answer = first_chapter_pages
    return answer