def solve():
    """Index: 1058.
    Returns: the total number of pages Tom reads in 7 days.
    """
    # L1
    total_reading_hours = 10 # Tom reads 10 hours
    initial_days = 5 # over 5 days
    hours_per_day = total_reading_hours / initial_days

    # L2
    pages_per_hour = 50 # He can read 50 pages per hour
    pages_per_day = hours_per_day * pages_per_hour

    # L3
    target_days = 7 # in 7 days
    total_pages_in_7_days = pages_per_day * target_days

    # FA
    answer = total_pages_in_7_days
    return answer