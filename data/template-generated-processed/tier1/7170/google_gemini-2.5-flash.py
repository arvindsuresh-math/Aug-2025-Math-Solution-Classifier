def solve():
    """Index: 7170.
    Returns: the number of books Monica will read next year.
    """
    # L1
    books_last_year = 16 # 16 books last year
    multiplier_this_year = 2 # twice the number of books she read last year
    books_this_year = multiplier_this_year * books_last_year

    # L2
    multiplier_for_next_year_base = 2 # twice the number of books she read this year
    twice_this_year_books = multiplier_for_next_year_base * books_this_year

    # L3
    additional_next_year = 5 # 5 more
    books_next_year = twice_this_year_books + additional_next_year

    # FA
    answer = books_next_year
    return answer