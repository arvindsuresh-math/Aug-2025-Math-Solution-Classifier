def solve():
    """Index: 1359.
    Returns: the number of pages Carter can read in 1 hour.
    """
    # L1
    lucy_more_than_oliver = 20 # Lucy can read 20 more pages than Oliver
    oliver_pages = 40 # Oliver can read 40 pages
    lucy_pages = oliver_pages + lucy_more_than_oliver

    # L2
    half_divisor = 2 # half as many pages
    carter_pages = lucy_pages / half_divisor

    # FA
    answer = carter_pages
    return answer