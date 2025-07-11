def solve():
    """Index: 1877.
    Returns: the total number of pages Maya read.
    """
    # L1
    books_last_week = 5 # Last week she read 5 books
    pages_per_book = 300 # Each book had 300 pages of text
    pages_last_week = books_last_week * pages_per_book

    # L2
    multiplier_this_week = 2 # This week she read twice as much
    pages_this_week = multiplier_this_week * pages_last_week

    # L3
    total_pages = pages_last_week + pages_this_week

    # FA
    answer = total_pages
    return answer