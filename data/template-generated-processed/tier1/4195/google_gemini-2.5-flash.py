def solve():
    """Index: 4195.
    Returns: the total number of books Katy read during the summer.
    """
    # L1
    books_june = 8 # 8 books in June
    multiplier_july = 2 # twice as many in July
    books_july = multiplier_july * books_june

    # L2
    fewer_august = 3 # three fewer in August
    books_august = books_july - fewer_august

    # L3
    total_books = books_june + books_july + books_august

    # FA
    answer = total_books
    return answer