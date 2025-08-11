def solve():
    """Index: 131.
    Returns: the total number of pages that Mitchell had read altogether.
    """
    # L1
    num_chapters_initial = 10 # read ten chapters of a book
    pages_per_chapter = 40 # each chapter in the book had 40 pages
    pages_from_first_ten_chapters = num_chapters_initial * pages_per_chapter

    # L2
    pages_in_11th_chapter = 20 # read 20 pages of the 11th chapter
    total_pages_after_11th_chapter_partial = pages_from_first_ten_chapters + pages_in_11th_chapter

    # L3
    num_additional_chapters = 2 # read 2 more chapters
    pages_from_additional_chapters = num_additional_chapters * pages_per_chapter

    # L4
    total_pages_read = total_pages_after_11th_chapter_partial + pages_from_additional_chapters

    # FA
    answer = total_pages_read
    return answer