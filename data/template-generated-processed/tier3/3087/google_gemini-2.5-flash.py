def solve():
    """Index: 3087.
    Returns: the number of additional pages Jessy should read per day.
    """
    # L1
    total_pages = 140 # a 140-page book
    reading_days = 7 # in one week
    required_pages_per_day = total_pages / reading_days

    # L2
    reads_per_day = 3 # read 3 times daily
    pages_per_read = 6 # 6 pages each time
    planned_pages_per_day = reads_per_day * pages_per_read

    # L3
    additional_pages_needed = required_pages_per_day - planned_pages_per_day

    # FA
    answer = additional_pages_needed
    return answer