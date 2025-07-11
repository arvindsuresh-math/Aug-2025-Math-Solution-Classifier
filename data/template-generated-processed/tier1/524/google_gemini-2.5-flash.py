def solve():
    """Index: 524.
    Returns: the number of books in the library now.
    """
    # L1
    initial_books = 336 # 336 books in a library
    books_taken_out_monday = 124 # 124 books are taken out
    books_after_monday = initial_books - books_taken_out_monday

    # L2
    books_brought_back_tuesday = 22 # 22 books are brought back
    books_after_tuesday = books_after_monday + books_brought_back_tuesday

    # FA
    answer = books_after_tuesday
    return answer