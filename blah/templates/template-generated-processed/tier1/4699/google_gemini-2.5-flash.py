def solve():
    """Index: 4699.
    Returns: the number of books Carlos read in June to meet his goal.
    """
    # L1
    books_july = 28 # 28 books in July
    books_august = 30 # 30 books in August
    books_july_august = books_july + books_august

    # L2
    total_needed = 100 # needed to read 100 books
    books_june = total_needed - books_july_august

    # FA
    answer = books_june
    return answer