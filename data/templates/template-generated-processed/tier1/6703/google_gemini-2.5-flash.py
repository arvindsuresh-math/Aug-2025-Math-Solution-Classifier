def solve():
    """Index: 6703.
    Returns: the number of books Suzy had at the end.
    """
    # L1
    initial_books = 98 # 98 books ready for checkout
    checked_out_wednesday = 43 # 43 books were checked out
    books_after_wednesday_checkout = initial_books - checked_out_wednesday

    # L2
    returned_thursday = 23 # 23 books were returned
    books_after_thursday_return = books_after_wednesday_checkout + returned_thursday

    # L3
    checked_out_thursday = 5 # 5 books were checked out
    books_after_thursday_checkout = books_after_thursday_return - checked_out_thursday

    # L4
    returned_friday = 7 # 7 books were returned
    final_books = books_after_thursday_checkout + returned_friday

    # FA
    answer = final_books
    return answer