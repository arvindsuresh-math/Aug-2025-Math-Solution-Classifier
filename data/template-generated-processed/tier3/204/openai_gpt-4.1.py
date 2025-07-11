def solve():
    """Index: 204.
    Returns: the average number of pages in each book.
    """
    # L1
    pages_per_inch = 80 # 80 pages is one inch thick
    total_inches = 12 # stack of books that is 12 inches thick
    total_pages = pages_per_inch * total_inches

    # L2
    num_books = 6 # he has 6 books
    average_pages_per_book = total_pages / num_books

    # FA
    answer = average_pages_per_book
    return answer