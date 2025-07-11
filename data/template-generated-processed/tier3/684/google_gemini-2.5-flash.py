def solve():
    """Index: 684.
    Returns: the time it would take Grace to finish reading the new book.
    """
    # L1
    total_pages_initial_book = 200 # a 200-page book
    time_to_read_initial_book = 20 # in 20 hours
    pages_per_hour = total_pages_initial_book / time_to_read_initial_book

    # L2
    pages_new_book = 250 # a 250-page book
    time_to_read_new_book = pages_new_book / pages_per_hour

    # FA
    answer = time_to_read_new_book
    return answer