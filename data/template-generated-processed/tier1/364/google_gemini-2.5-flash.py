def solve():
    """Index: 364.
    Returns: the total number of books Stu and Albert have.
    """
    # L1
    albert_multiplier = 4 # 4 times as many books as Stu
    stu_books = 9 # Stu has 9 books
    albert_books = albert_multiplier * stu_books

    # L2
    total_books = albert_books + stu_books

    # FA
    answer = total_books
    return answer