def solve():
    """Index: 1053.
    Returns: the total number of pages Jane will read in a week.
    """
    # L1
    morning_pages = 5 # she reads 5 pages in the morning
    evening_pages = 10 # she reads 10 pages in the evening
    pages_per_day = evening_pages + morning_pages

    # L2
    days_in_week = 7 # WK
    total_pages = pages_per_day * days_in_week

    # FA
    answer = total_pages
    return answer