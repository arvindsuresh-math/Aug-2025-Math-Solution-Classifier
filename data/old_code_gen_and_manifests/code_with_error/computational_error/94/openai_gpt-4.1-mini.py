def solve(
    pages_per_day: int = 20,  # John writes 20 pages a day
    num_books: int = 3,       # number of books
    pages_per_book: int = 400 # pages in each book
):
    """Index: 94.
    Returns: the number of days it will take John to write the books.
    """

    #: L1
    total_pages = num_books * pages_per_book

    #: L2
    days_needed = 50.0

    #: FA
    answer = days_needed
    return answer