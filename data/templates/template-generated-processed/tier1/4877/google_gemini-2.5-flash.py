def solve():
    """Index: 4877.
    Returns: the number of old books Brianna will have to reread this year.
    """
    # L1
    months_per_year = 12 # WK
    books_per_month = 2 # reads two books a month
    books_needed_per_year = months_per_year * books_per_month

    # L2
    books_bought = 8 # bought eight new books
    fewer_borrowed_than_bought = 2 # borrow two fewer new books than she bought
    books_borrowed = books_bought - fewer_borrowed_than_bought

    # L3
    books_given = 6 # given six new books as a gift
    total_new_books = books_given + books_bought + books_borrowed

    # L4
    books_to_reread = books_needed_per_year - total_new_books

    # FA
    answer = books_to_reread
    return answer