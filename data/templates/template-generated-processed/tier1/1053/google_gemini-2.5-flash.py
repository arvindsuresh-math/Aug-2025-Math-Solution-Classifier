def solve():
    """Index: 1053.
    Returns: the total number of pages Jane will read in a week.
    """
    # L1
    morning_pages = 5 # reads 5 pages
    evening_pages = 10 # reads 10 pages
    pages_per_day = evening_pages + morning_pages

    # L2
    days_in_week = 7 # WK
    total_pages_in_week = pages_per_day * days_in_week

    # FA
    answer = total_pages_in_week
    return answer