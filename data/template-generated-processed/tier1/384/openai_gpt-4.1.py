def solve():
    """Index: 384.
    Returns: the number of pages Nico read on Wednesday.
    """
    # L1
    monday_pages = 20 # reads the first book with a total of 20 pages
    tuesday_pages = 12 # reads the second book with a total of 12 pages
    mon_tue_total = monday_pages + tuesday_pages

    # L2
    total_pages = 51 # he has read a total of 51 pages from Monday to Wednesday
    wednesday_pages = total_pages - mon_tue_total

    # FA
    answer = wednesday_pages
    return answer