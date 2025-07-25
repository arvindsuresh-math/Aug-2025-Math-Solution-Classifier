def solve():
    """Index: 318.
    Returns: the number of books Roselyn had initially.
    """
    # L1
    rebecca_books = 40 # Rebecca received 40 books
    mara_multiplier = 3 # three times as many books
    mara_books = mara_multiplier * rebecca_books

    # L2
    total_given_books = mara_books + rebecca_books

    # L3
    remaining_books = 60 # remains with 60 books
    initial_books = remaining_books + total_given_books

    # FA
    answer = initial_books
    return answer