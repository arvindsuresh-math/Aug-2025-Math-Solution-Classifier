from fractions import Fraction

def solve():
    """Index: 276.
    Returns: the total number of pages Sabrina has to read to finish the whole series.
    """
    # L1
    total_books = 14 # 14 books in the series
    pages_per_book = 200 # each book has 200 pages
    total_pages = total_books * pages_per_book

    # L2
    books_read_first_month = 4 # read four books in a month
    pages_read_first_month = books_read_first_month * pages_per_book

    # L3
    books_remaining_after_first_month = total_books - books_read_first_month

    # L4
    second_month_fraction = Fraction(1, 2) # half the number of books remaining
    books_read_second_month = second_month_fraction * books_remaining_after_first_month

    # L5
    pages_read_second_month = books_read_second_month * pages_per_book

    # L6
    pages_read_two_months = pages_read_second_month + pages_read_first_month

    # L7
    pages_left_to_read = total_pages - pages_read_two_months

    # FA
    answer = pages_left_to_read
    return answer