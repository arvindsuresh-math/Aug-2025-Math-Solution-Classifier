def solve():
    """Index: 3561.
    Returns: the number of pages in the science book.
    """
    # L1
    history_book_pages = 300 # history book has 300 pages
    half_divisor = 2 # half as many pages
    novel_pages = history_book_pages / half_divisor

    # L2
    science_book_multiplier = 4 # 4 times the amount of pages
    science_book_pages = science_book_multiplier * novel_pages

    # FA
    answer = science_book_pages
    return answer