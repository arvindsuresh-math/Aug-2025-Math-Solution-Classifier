def solve(
        history_books: int = 12, # She shelved 12 history books
        romance_books: int = 8, # 8 romance books
        poetry_books: int = 4, # and 4 poetry books
        western_novels: int = 5, # including 5 Western novels
        biographies: int = 6 # and 6 biographies
    ):
    """Index: 97.
    Returns: the total number of books on the book cart when Nancy started.
    """

    #: L1
    mystery_books = western_novels + biographies

    #: L2
    total_books = history_books + romance_books + poetry_books + mystery_books + western_novels + biographies

    #: FA
    answer = total_books
    return answer