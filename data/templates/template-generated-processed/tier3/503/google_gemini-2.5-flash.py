def solve():
    """Index: 503.
    Returns: the number of pages Yasna needs to read every day.
    """
    # L1
    book_one_pages = 180 # One book is 180 pages long
    book_two_pages = 100 # the other book is 100 pages long
    total_pages = book_one_pages + book_two_pages

    # L2
    total_reading_days = 14 # in two weeks
    pages_per_day = total_pages / total_reading_days

    # FA
    answer = pages_per_day
    return answer