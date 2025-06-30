def solve(
        pages_per_day: int = 20, # John writes 20 pages a day
        num_books: int = 3, # 3 books
        pages_per_book: int = 400 # 400 pages each
    ):
    """Index: 94.
    Returns: the number of days it will take John to write the books.
    """

    #: L1
    total_pages_to_write = num_books * pages_per_book # eval: 1200 = 3 * 400

    #: L2
    days_to_write = total_pages_to_write / pages_per_day # eval: 60.0 = 1200 / 20

    #: FA
    answer = days_to_write # eval: 60.0 = 60.0
    return answer # eval: return 60.0
