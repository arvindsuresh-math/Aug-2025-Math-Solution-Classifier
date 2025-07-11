def solve():
    """Index: 780.
    Returns: the number of pages Tom could read in 2 hours at triple speed.
    """
    # L1
    pages_per_hour = 12 # Tom can read 12 pages of a book in one hour
    speed_factor = 3 # increase his reading speed by a factor of 3
    pages_per_hour_tripled = pages_per_hour * speed_factor

    # L2
    hours = 2 # during 2 hours
    total_pages = pages_per_hour_tripled * hours

    # FA
    answer = total_pages
    return answer