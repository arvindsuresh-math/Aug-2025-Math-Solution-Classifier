from fractions import Fraction

def solve():
    """Index: 3036.
    Returns: Lovely's total earnings from selling all books.
    """
    # L1
    total_books = 10 # all 10 books
    fraction_books_2_50 = Fraction(2, 5) # Two-fifths of Lovely's books
    books_at_2_50 = total_books * fraction_books_2_50

    # L2
    books_at_2 = total_books - books_at_2_50

    # L3
    price_per_book_2_50 = 2.50 # $2.50 each
    earnings_from_2_50_books = price_per_book_2_50 * books_at_2_50

    # L4
    price_per_book_2 = 2 # $2 each
    earnings_from_2_books = price_per_book_2 * books_at_2

    # L5
    total_earnings = earnings_from_2_50_books + earnings_from_2_books

    # FA
    answer = total_earnings
    return answer