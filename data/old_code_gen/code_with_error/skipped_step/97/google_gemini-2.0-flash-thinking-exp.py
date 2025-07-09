def solve(
    history_books: int = 12, # She shelved 12 history books
    romance_books: int = 8, # 8 romance books
    poetry_books: int = 4, # and 4 poetry books
    fraction_mystery_books: float = 0.5, # Half the books on the bottom section of the cart were mystery books
    western_novels: int = 5, # including 5 Western novels
    biographies: int = 6 # and 6 biographies
):
    """Index: 97.
    Returns: the total number of books on the cart when she started.
    """

    #: L1
    mystery_books = western_novels + biographies

    #: L2

    #: FA
    answer = poetry_books
    return answer