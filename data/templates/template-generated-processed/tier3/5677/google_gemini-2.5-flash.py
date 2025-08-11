def solve():
    """Index: 5677.
    Returns: the total time in minutes it would take Tom to type out 10 pages.
    """
    # L1
    words_per_page = 450 # A page is 450 words
    words_per_minute = 90 # Tom can type 90 words a minute
    minutes_per_page = words_per_page / words_per_minute

    # L2
    num_pages = 10 # type out 10 pages
    total_time_minutes = minutes_per_page * num_pages

    # FA
    answer = total_time_minutes
    return answer