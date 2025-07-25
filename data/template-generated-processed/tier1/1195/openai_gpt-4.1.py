def solve():
    """Index: 1195.
    Returns: the total number of books in the library now.
    """
    # L1
    books_before_last_year = 100 # library had 100 books before it purchased new books last year
    books_purchased_last_year = 50 # purchased 50 new books last year
    total_after_last_year = books_before_last_year + books_purchased_last_year

    # L2
    times_more_this_year = 3 # purchased 3 times as many books this year
    books_purchased_this_year = books_purchased_last_year * times_more_this_year

    # L3
    total_books_now = total_after_last_year + books_purchased_this_year

    # FA
    answer = total_books_now
    return answer