def solve(
    pages_per_day: int = 20, # John writes 20 pages a day.
    num_books: int = 3, # 3 books
    pages_per_book: int = 400 # that are 400 pages each
):
    """Index: 94.
    Returns: the number of days it will take John to write 3 books.
    """

    #: L1
    total_pages_to_write = pages_per_day * pages_per_book # eval: 8000 = 20 * 400

    #: L2
    days_to_write = total_pages_to_write / pages_per_day # eval: 400.0 = 8000 / 20

    #: FA
    answer = days_to_write
    return answer # eval: return 400.0
