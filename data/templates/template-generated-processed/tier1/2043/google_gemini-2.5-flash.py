def solve():
    """Index: 2043.
    Returns: the difference in books read between Brad and William across two months.
    """
    # L1
    william_last_month = 6 # William read 6 books last month
    multiplier_thrice = 3 # thrice as many books
    brad_last_month = multiplier_thrice * william_last_month

    # L2
    brad_this_month = 8 # Brad, who read 8 books
    multiplier_twice = 2 # twice as much as Brad
    william_this_month = multiplier_twice * brad_this_month

    # L3
    total_brad_books = brad_last_month + brad_this_month

    # L4
    total_william_books = william_last_month + william_this_month

    # L5
    difference_in_books = total_brad_books - total_william_books

    # FA
    answer = difference_in_books
    return answer