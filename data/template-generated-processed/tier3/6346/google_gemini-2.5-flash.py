from fractions import Fraction

def solve():
    """Index: 6346.
    Returns: the total number of pages in the book.
    """
    # L1
    pages_per_day = 8 # He read 8 pages every day
    days_read = 12 # by the 12th of April
    total_pages_read = pages_per_day * days_read

    # L3
    inverse_fraction_covered = Fraction(3, 2) # two-thirds of the book (implies 2/3, so inverse is 3/2)
    total_book_pages = total_pages_read * inverse_fraction_covered

    # FA
    answer = total_book_pages
    return answer