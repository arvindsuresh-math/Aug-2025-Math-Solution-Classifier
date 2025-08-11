def solve():
    """Index: 4703.
    Returns: the total number of pages in all of Suzanna's textbooks.
    """
    # L1
    history_pages = 160 # 160 pages
    geography_extra_pages = 70 # 70 more pages
    geography_pages = history_pages + geography_extra_pages

    # L2
    history_geography_sum = history_pages + geography_pages

    # L3
    math_divisor = 2 # half of the sum
    math_pages = history_geography_sum / math_divisor

    # L4
    science_multiplier = 2 # twice the number
    science_pages = history_pages * science_multiplier

    # L5
    total_pages = history_pages + geography_pages + math_pages + science_pages

    # FA
    answer = total_pages
    return answer