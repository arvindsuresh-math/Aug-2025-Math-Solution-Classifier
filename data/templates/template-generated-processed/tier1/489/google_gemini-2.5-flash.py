def solve():
    """Index: 489.
    Returns: the difference in the bookstore's earnings on the two books.
    """
    # L1
    num_top_books_sold = 13 # Thirteen "TOP" books
    cost_top_book = 8 # "TOP," costs $8
    earnings_top_books = num_top_books_sold * cost_top_book

    # L2
    num_abc_books_sold = 4 # four "ABC" books
    cost_abc_book = 23 # "ABC," costs $23
    earnings_abc_books = num_abc_books_sold * cost_abc_book

    # L3
    difference_in_earnings = earnings_top_books - earnings_abc_books

    # FA
    answer = difference_in_earnings
    return answer