def solve():
    """Index: 5650.
    Returns: the difference in pages read by Dustin and Sam in 40 minutes.
    """
    # L1
    dustin_pages_per_hour = 75 # Dustin can read 75 pages in an hour
    minutes_per_hour = 60 # WK
    dustin_pages_per_minute = dustin_pages_per_hour / minutes_per_hour

    # L2
    reading_time_minutes = 40 # in 40 minutes
    dustin_total_pages = reading_time_minutes * dustin_pages_per_minute

    # L3
    sam_pages_per_hour = 24 # Sam can read 24 pages in an hour
    sam_pages_per_minute = sam_pages_per_hour / minutes_per_hour

    # L4
    sam_total_pages = reading_time_minutes * sam_pages_per_minute

    # L5
    page_difference = dustin_total_pages - sam_total_pages

    # FA
    answer = page_difference
    return answer