def solve():
    """Index: 222.
    Returns: the number of pages Bekah needs to read each day.
    """
    # L1
    total_pages = 408 # 408 pages for history class
    pages_read_weekend = 113 # She read 113 pages over the weekend
    pages_left_to_read = total_pages - pages_read_weekend

    # L2
    days_left = 5 # has 5 days left
    pages_per_day = pages_left_to_read / days_left

    # FA
    answer = pages_per_day
    return answer