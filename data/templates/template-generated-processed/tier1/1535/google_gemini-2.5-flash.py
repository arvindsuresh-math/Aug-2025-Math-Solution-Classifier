def solve():
    """Index: 1535.
    Returns: the total number of pages Janine read in two months.
    """
    # L1
    books_last_month = 5 # 5 books last month
    multiplier_this_month = 2 # twice as many books
    books_this_month = books_last_month * multiplier_this_month

    # L2
    total_books = books_last_month + books_this_month

    # L3
    pages_per_book = 10 # each book has 10 pages
    total_pages = total_books * pages_per_book

    # FA
    answer = total_pages
    return answer