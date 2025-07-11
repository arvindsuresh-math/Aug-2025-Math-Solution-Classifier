def solve():
    """Index: 780.
    Returns: the total number of pages Tom can read in two hours with increased speed.
    """
    # L1
    initial_pages_per_hour = 12 # 12 pages of a book
    speed_increase_factor = 3 # increase his reading speed by a factor of 3
    new_pages_per_hour = initial_pages_per_hour * speed_increase_factor

    # L2
    reading_time_hours = 2 # during 2 hours
    total_pages_read = new_pages_per_hour * reading_time_hours

    # FA
    answer = total_pages_read
    return answer