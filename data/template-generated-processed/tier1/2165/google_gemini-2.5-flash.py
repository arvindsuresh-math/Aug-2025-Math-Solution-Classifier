def solve():
    """Index: 2165.
    Returns: the number of pages still left to be read.
    """
    # L1
    pages_per_day = 20 # reads 20 pages a day
    days_in_week = 7 # WK
    pages_read_in_week = pages_per_day * days_in_week

    # L2
    pages_already_read = 149 # already read 149 pages
    total_pages_read = pages_already_read + pages_read_in_week

    # L3
    total_pages_in_book = 381 # 381 pages in Elliot’s book
    pages_left_to_read = total_pages_in_book - total_pages_read

    # FA
    answer = pages_left_to_read
    return answer