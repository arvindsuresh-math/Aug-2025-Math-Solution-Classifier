def solve():
    """Index: 6582.
    Returns: the number of pages in the old edition Geometry book.
    """
    # L3
    new_edition_pages = 450 # 450 pages
    pages_less = 230 # 230 pages less
    value_of_2x = new_edition_pages + pages_less

    # L5
    multiplier_for_twice = 2 # twice as many pages
    old_edition_pages = value_of_2x / multiplier_for_twice

    # FA
    answer = old_edition_pages
    return answer