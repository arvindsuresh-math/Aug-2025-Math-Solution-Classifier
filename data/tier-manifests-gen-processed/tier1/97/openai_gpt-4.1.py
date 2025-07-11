def solve():
    """Index: 97.
    Returns: the total number of books Nancy had on the book cart when she started.
    """
    # L1
    western_novels = 5 # 5 Western novels
    biographies = 6 # 6 biographies
    mystery_books = western_novels + biographies

    # L2
    history_books = 12 # 12 history books
    romance_books = 8 # 8 romance books
    poetry_books = 4 # 4 poetry books
    total_books = history_books + romance_books + poetry_books + mystery_books + western_novels + biographies

    # FA
    answer = total_books
    return answer