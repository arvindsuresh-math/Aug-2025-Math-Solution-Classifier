def solve():
    """Index: 1195.
    Returns: the total number of books in the library now.
    """
    # L1
    books_before_last_year = 100 # 100 books before it purchased new books last year
    books_purchased_last_year = 50 # purchased 50 new books
    total_books_after_last_year_purchase = books_before_last_year + books_purchased_last_year

    # L2
    multiplier_this_year = 3 # 3 times as many books
    books_purchased_this_year = books_purchased_last_year * multiplier_this_year

    # L3
    total_books_now = total_books_after_last_year_purchase + books_purchased_this_year

    # FA
    answer = total_books_now
    return answer