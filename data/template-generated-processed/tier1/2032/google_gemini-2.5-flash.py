def solve():
    """Index: 2032.
    Returns: the number of books remaining in the library.
    """
    # L1
    initial_books = 250 # 250 books inside a library
    books_taken_out_tuesday = 120 # 120 books are taken out
    books_after_tuesday = initial_books - books_taken_out_tuesday

    # L2
    books_returned_wednesday = 35 # 35 books are returned
    books_after_wednesday = books_after_tuesday + books_returned_wednesday

    # L3
    books_withdrawn_thursday = 15 # another 15 books are withdrawn from the library
    final_books = books_after_wednesday - books_withdrawn_thursday

    # FA
    answer = final_books
    return answer