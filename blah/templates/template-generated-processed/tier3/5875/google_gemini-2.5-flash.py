def solve():
    """Index: 5875.
    Returns: the total number of pages Lana has in her binder.
    """
    # L1
    duane_total_pages = 42 # 42 pages in his binder
    half_divisor = 2 # half of the 42 pages
    pages_from_duane = duane_total_pages / half_divisor

    # L2
    lana_initial_pages = 8 # 8 blank pages left in her binder
    lana_total_pages = pages_from_duane + lana_initial_pages

    # FA
    answer = lana_total_pages
    return answer