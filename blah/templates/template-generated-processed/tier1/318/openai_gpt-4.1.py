def solve():
    """Index: 318.
    Returns: the number of books Roselyn had before.
    """
    # L1
    rebecca_books = 40 # Rebecca received 40 books
    mara_multiplier = 3 # Mara three times as many books as Rebecca
    mara_books = mara_multiplier * rebecca_books

    # L2
    total_given = mara_books + rebecca_books

    # L3
    roselyn_remaining = 60 # remains with 60 books
    roselyn_initial = roselyn_remaining + total_given

    # FA
    answer = roselyn_initial
    return answer