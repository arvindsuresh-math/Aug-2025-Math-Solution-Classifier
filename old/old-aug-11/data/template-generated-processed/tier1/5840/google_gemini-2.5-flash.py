def solve():
    """Index: 5840.
    Returns: the number of pages worth of books Phil has left.
    """
    # L1
    initial_books = 10 # 10 books
    lost_books = 2 # 2 books are lost
    remaining_books = initial_books - lost_books

    # L2
    pages_per_book = 100 # 100 pages each
    total_remaining_pages = remaining_books * pages_per_book

    # FA
    answer = total_remaining_pages
    return answer