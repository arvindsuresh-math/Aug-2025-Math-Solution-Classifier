def solve():
    """Index: 5310.
    Returns: the number of books Sarah should check out.
    """
    # L1
    words_per_page = 100 # 100 words per page
    pages_per_book = 80 # 80 pages long
    words_per_book = words_per_page * pages_per_book

    # L2
    words_per_minute = 40 # 40 words per minute
    minutes_per_book = words_per_book / words_per_minute

    # L3
    reading_hours = 20 # 20 hours
    minutes_per_hour = 60 # WK
    total_reading_minutes = reading_hours * minutes_per_hour

    # L4
    num_books = total_reading_minutes / minutes_per_book

    # FA
    answer = num_books
    return answer