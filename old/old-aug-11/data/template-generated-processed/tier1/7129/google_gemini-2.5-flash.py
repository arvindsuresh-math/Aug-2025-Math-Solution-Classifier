def solve():
    """Index: 7129.
    Returns: the number of books Mary currently has checked out of the library.
    """
    # L1
    initial_books = 5 # borrowed 5 books from the library
    returned_first_batch = 3 # returned 3 books
    books_after_first_return = initial_books - returned_first_batch

    # L2
    checked_out_first_new_batch = 5 # checked out 5 more books
    books_after_first_checkout = books_after_first_return + checked_out_first_new_batch

    # L3
    returned_second_batch = 2 # returned 2 of those books
    books_after_second_return = books_after_first_checkout - returned_second_batch

    # L4
    checked_out_second_new_batch = 7 # checked out 7 more books
    final_books = books_after_second_return + checked_out_second_new_batch

    # FA
    answer = final_books
    return answer