def solve():
    """Index: 14.
    Returns: the total hours it will take Joy to read the book.
    """
    # L2
    pages_per_interval = 8 # read 8 pages
    sets_of_minutes_per_hour = 3 # In one hour, there are 3 sets of 20 minutes
    pages_per_hour = pages_per_interval * sets_of_minutes_per_hour

    # L3
    total_pages_to_read = 120 # read 120 pages
    time_to_read_book_hours = total_pages_to_read / pages_per_hour

    # FA
    answer = time_to_read_book_hours
    return answer