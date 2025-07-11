def solve():
    """Index: 524.
    Returns: the number of books in the library after Tuesday.
    """
    # L1
    initial_books = 336 # 336 books in a library
    taken_out_monday = 124 # 124 books are taken out
    after_monday = initial_books - taken_out_monday

    # L2
    returned_tuesday = 22 # 22 books are brought back
    after_tuesday = after_monday + returned_tuesday

    # FA
    answer = after_tuesday
    return answer