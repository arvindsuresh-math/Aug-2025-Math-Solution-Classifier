def solve():
    """Index: 2486.
    Returns: the number of additional hours Joanna needs to read to finish the book.
    """
    # L1
    monday_hours = 3 # reads for 3 hours
    pages_per_hour = 16 # can read 16 pages per hour
    monday_pages_read = monday_hours * pages_per_hour

    # L2
    tuesday_hours = 6.5 # reads for 6.5 hours
    tuesday_pages_read = tuesday_hours * pages_per_hour

    # L3
    total_pages_read_so_far = monday_pages_read + tuesday_pages_read

    # L4
    total_pages_in_book = 248 # 248 pages in a book
    pages_left = total_pages_in_book - total_pages_read_so_far

    # L5
    hours_needed = pages_left / pages_per_hour

    # FA
    answer = hours_needed
    return answer