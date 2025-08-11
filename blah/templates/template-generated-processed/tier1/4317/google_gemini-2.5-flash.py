def solve():
    """Index: 4317.
    Returns: the total number of books Lily will finish for two months.
    """
    # L1
    books_last_month = 4 # 4 books last month
    multiplier_this_month = 2 # twice as many books
    books_this_month = books_last_month * multiplier_this_month

    # L2
    total_books_two_months = books_last_month + books_this_month

    # FA
    answer = total_books_two_months
    return answer