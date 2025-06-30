def solve(
    pages_per_day: int = 20, # John writes 20 pages a day
    num_books: int = 3, # to write 3 books
    pages_per_book: int = 400 # that are 400 pages each
):
    """Index: 94.
    Returns: the number of days it will take John to write the books.
    """

    #: L1
    total_pages = num_books * pages_per_book # eval: 1200 = 3 * 400

    #: L2
    days_needed = total_pages / pages_per_day # eval: 60.0 = 1200 / 20

    #: FA
    answer = days_needed
    return answer # eval: return 60.0
