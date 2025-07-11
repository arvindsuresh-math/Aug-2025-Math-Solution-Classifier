def solve():
    """Index: 131.
    Returns: the total number of pages Mitchell had read altogether.
    """
    # L1
    chapters_read_before_4 = 10 # read ten chapters of a book before 4 o'clock
    pages_per_chapter = 40 # each chapter in the book had 40 pages
    pages_first_ten = chapters_read_before_4 * pages_per_chapter

    # L2
    pages_read_ch11 = 20 # had read 20 pages of the 11th chapter
    pages_after_ch11 = pages_first_ten + pages_read_ch11

    # L3
    chapters_read_after_4 = 2 # read 2 more chapters of the book
    pages_next_two = chapters_read_after_4 * pages_per_chapter

    # L4
    total_pages = pages_after_ch11 + pages_next_two

    # FA
    answer = total_pages
    return answer