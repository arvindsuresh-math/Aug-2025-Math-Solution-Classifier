def solve():
    """Index: 5077.
    Returns: the number of pages Lance should read tomorrow to finish the book.
    """
    # L1
    pages_yesterday = 35 # read 35 pages
    fewer_pages_today = 5 # read 5 fewer pages than yesterday
    pages_today = pages_yesterday - fewer_pages_today

    # L2
    total_pages_two_days = pages_yesterday + pages_today

    # L3
    total_book_pages = 100 # a 100 page book
    pages_tomorrow = total_book_pages - total_pages_two_days

    # FA
    answer = pages_tomorrow
    return answer