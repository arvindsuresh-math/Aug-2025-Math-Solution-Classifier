def solve():
    """Index: 662.
    Returns: the total number of books owned by Harry, Flora, and Gary.
    """
    # L1
    harry_books = 50 # Harry has 50 books
    flora_books = harry_books * 2

    # L2
    gary_books = harry_books / 2

    # L3
    total_books = flora_books + gary_books + harry_books

    # FA
    answer = total_books
    return answer