from fractions import Fraction

def solve():
    """Index: 1592.
    Returns: the total number of books Betty and her sister have.
    """
    # L1
    sister_fraction_more = Fraction(1, 4) # 1/4 times more books
    betty_books = 20 # Betty has 20 books
    additional_sister_books = sister_fraction_more * betty_books

    # L2
    sister_total_books = betty_books + additional_sister_books

    # L3
    total_books = sister_total_books + betty_books

    # FA
    answer = total_books
    return answer