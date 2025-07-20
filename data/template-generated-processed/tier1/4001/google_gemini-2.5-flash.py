def solve():
    """Index: 4001.
    Returns: the number of more pages Liza reads than Suzie in 3 hours.
    """
    # L1
    liza_pages_per_hour = 20 # 20 pages in an hour
    hours = 3 # 3 hours
    liza_total_pages = liza_pages_per_hour * hours

    # L2
    suzie_pages_per_hour = 15 # 15 pages in an hour
    suzie_total_pages = suzie_pages_per_hour * hours

    # L3
    difference_pages = liza_total_pages - suzie_total_pages

    # FA
    answer = difference_pages
    return answer