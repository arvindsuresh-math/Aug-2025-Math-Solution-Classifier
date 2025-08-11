def solve():
    """Index: 364.
    Returns: the total number of books Stu and Albert have together.
    """
    # L1
    stu_books = 9 # Stu has 9 books
    albert_multiplier = 4 # Albert has 4 times as many books as Stu
    albert_books = albert_multiplier * stu_books

    # L2
    total_books = albert_books + stu_books

    # FA
    answer = total_books
    return answer