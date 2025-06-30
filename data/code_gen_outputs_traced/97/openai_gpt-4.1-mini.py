def solve(
    history_books: int = 12,  # 12 history books shelved from top section
    romance_books: int = 8,   # 8 romance books shelved from top section
    poetry_books: int = 4,    # 4 poetry books shelved from top section
    western_novels: int = 5,  # 5 Western novels shelved from bottom section
    biographies: int = 6      # 6 biographies shelved from bottom section
):
    """Index: 97.
    Returns: the total number of books Nancy had on the book cart when she started.
    """

    #: L1
    mystery_books = western_novels + biographies # eval: 11 = 5 + 6

    #: L2
    total_books = history_books + romance_books + poetry_books + mystery_books + western_novels + biographies # eval: 46 = 12 + 8 + 4 + 11 + 5 + 6

    #: FA
    answer = total_books # eval: 46 = 46
    return answer # eval: return 46
