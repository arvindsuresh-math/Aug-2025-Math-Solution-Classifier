def solve():
    """Index: 2869.
    Returns: the number of pages remaining in the pad.
    """
    # L1
    science_percent_decimal = 0.25 # uses 25% of the pages
    total_pages = 120 # new pad of paper has 120 pages
    pages_for_science = science_percent_decimal * total_pages

    # L2
    pages_after_science = total_pages - pages_for_science

    # L3
    pages_for_math = 10 # another 10 pages
    pages_remaining = pages_after_science - pages_for_math

    # FA
    answer = pages_remaining
    return answer