def solve():
    """Index: 384.
    Returns: the number of pages Nico read on Wednesday.
    """
    # L1
    pages_monday = 20 # 20 pages
    pages_tuesday = 12 # 12 pages
    pages_mon_tue = pages_monday + pages_tuesday

    # L2
    total_pages_mon_wed = 51 # total of 51 pages from Monday to Wednesday
    pages_wednesday = total_pages_mon_wed - pages_mon_tue

    # FA
    answer = pages_wednesday
    return answer