def solve():
    """Index: 222.
    Returns: the number of pages Bekah needs to read each day for 5 days to complete her assignment.
    """
    # L1
    total_pages = 408 # Bekah had to read 408 pages for history class
    pages_read = 113 # She read 113 pages over the weekend
    pages_left = total_pages - pages_read

    # L2
    days_left = 5 # has 5 days left to finish her reading
    pages_per_day = pages_left / days_left

    # FA
    answer = pages_per_day
    return answer