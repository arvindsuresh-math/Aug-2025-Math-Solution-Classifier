def solve():
    """Index: 97.
    Returns: the total number of books on the book cart when Nancy started.
    """
    # L1
    western_novels = 5 # 5 Western novels
    biographies = 6 # 6 biographies
    mystery_novels = western_novels + biographies

    # L2
    history_books = 12 # 12 history books
    romance_books = 8 # 8 romance books
    poetry_books = 4 # 4 poetry books
    total_books = history_books + romance_books + poetry_books + mystery_novels + western_novels + biographies

    # FA
    answer = total_books
    return answer