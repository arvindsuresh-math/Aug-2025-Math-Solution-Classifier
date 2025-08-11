def solve():
    """Index: 2165.
    Returns: the number of pages still left to be read in Elliot's book.
    """
    # L1
    pages_per_day = 20 # If he reads 20 pages a day
    days_in_week = 7 # WK
    pages_in_week = pages_per_day * days_in_week

    # L2
    pages_already_read = 149 # He has already read 149 pages
    total_pages_read = pages_already_read + pages_in_week

    # L3
    total_pages = 381 # There are 381 pages in Elliot’s book
    pages_left = total_pages - total_pages_read

    # FA
    answer = pages_left
    return answer