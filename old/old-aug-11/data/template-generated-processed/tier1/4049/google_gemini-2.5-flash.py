def solve():
    """Index: 4049.
    Returns: the number of pages Ethan has left to read.
    """
    # L1
    pages_read_saturday_morning = 40 # 40 pages on Saturday morning
    pages_read_saturday_night = 10 # another 10 pages at night
    total_pages_saturday = pages_read_saturday_morning + pages_read_saturday_night

    # L2
    multiplier_next_day = 2 # twice the total pages as on Saturday
    pages_read_next_day = total_pages_saturday * multiplier_next_day

    # L3
    total_pages_read = total_pages_saturday + pages_read_next_day

    # L4
    total_book_pages = 360 # 360 pages
    pages_left_to_read = total_book_pages - total_pages_read

    # FA
    answer = pages_left_to_read
    return answer