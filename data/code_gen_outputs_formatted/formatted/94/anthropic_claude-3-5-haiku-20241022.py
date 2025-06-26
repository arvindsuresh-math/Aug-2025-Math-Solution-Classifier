def solve(
    pages_per_day: int = 20,  # John writes 20 pages a day
    num_books: int = 3,  # 3 books
    pages_per_book: int = 400  # each book is 400 pages
):
    """Index: 94.
    Returns: the number of days it will take John to write the books."""

    #: L1
    total_pages = num_books * pages_per_book

    #: L2
    days_to_complete = total_pages / pages_per_day

    answer = days_to_complete  # FINAL ANSWER
    return answer