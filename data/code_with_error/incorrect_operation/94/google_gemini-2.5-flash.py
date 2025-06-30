def solve(
        pages_per_day: int = 20, # John writes 20 pages a day
        num_books: int = 3, # 3 books
        pages_per_book: int = 400 # 400 pages each
    ):
    """Index: 94.
    Returns: the number of days it will take John to write the books.
    """

    #: L1
    total_pages_to_write = num_books - pages_per_book

    #: L2
    days_to_write = total_pages_to_write / pages_per_day

    #: FA
    answer = days_to_write
    return answer