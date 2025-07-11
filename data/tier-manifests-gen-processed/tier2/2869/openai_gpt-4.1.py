def solve():
    """Index: 2869.
    Returns: the number of pages remaining in the pad after Sammy's usage.
    """
    # L1
    science_percent = 0.25 # 25% of the pages for his science project
    total_pages = 120 # new pad of paper has 120 pages
    science_pages = science_percent * total_pages

    # L2
    pages_after_science = total_pages - science_pages

    # L3
    math_pages = 10 # another 10 pages for his math homework
    pages_after_math = pages_after_science - math_pages

    # FA
    answer = pages_after_math
    return answer