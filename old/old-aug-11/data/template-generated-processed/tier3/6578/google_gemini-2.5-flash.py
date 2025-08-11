def solve():
    """Index: 6578.
    Returns: the number of books sold by the library.
    """
    # L1
    total_books = 9900 # The library has 9,900 books
    fraction_denominator = 6 # four sixths of the books
    one_sixth_books = total_books / fraction_denominator

    # L2
    fraction_numerator = 4 # four sixths of the books
    books_left = fraction_numerator * one_sixth_books

    # L3
    books_sold = total_books - books_left

    # FA
    answer = books_sold
    return answer