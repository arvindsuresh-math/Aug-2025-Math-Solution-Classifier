def solve():
    """Index: 276.
    Returns: the total number of pages Sabrina has to read to finish the whole series.
    """
    # L1
    total_books_in_series = 14 # 14 books in the series
    pages_per_book = 200 # each book has 200 pages
    total_pages_series = total_books_in_series * pages_per_book

    # L2
    books_read_first_month = 4 # She read four books in a month
    pages_read_first_month = books_read_first_month * pages_per_book

    # L3
    books_remaining_after_first_month = total_books_in_series - books_read_first_month

    # L4
    half_numerator = 1 # half the number of books remaining
    half_denominator = 2 # half the number of books remaining
    books_read_second_month = (half_numerator / half_denominator) * books_remaining_after_first_month

    # L5
    pages_read_second_month = books_read_second_month * pages_per_book

    # L6
    total_pages_read = pages_read_second_month + pages_read_first_month

    # L7
    pages_to_read_to_finish = total_pages_series - total_pages_read

    # FA
    answer = pages_to_read_to_finish
    return answer