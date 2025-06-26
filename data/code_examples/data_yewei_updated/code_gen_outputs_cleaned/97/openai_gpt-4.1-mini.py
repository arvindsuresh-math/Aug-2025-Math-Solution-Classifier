def solve(
    history_books: int = 12,  # shelved 12 history books
    romance_books: int = 8,   # shelved 8 romance books
    poetry_books: int = 4,    # shelved 4 poetry books
    western_novels: int = 5,  # shelved 5 Western novels from bottom section
    biographies: int = 6      # shelved 6 biographies from bottom section
):
    """Index: 97.
    Returns: the total number of books Nancy had on the book cart when she started.
    """
    #: L1
    mystery_books = western_novels + biographies  # half the books on bottom section are mystery books

    #: L2
    total_books = history_books + romance_books + poetry_books + mystery_books + western_novels + biographies

    answer = total_books  # FINAL ANSWER
    return answer