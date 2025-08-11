def solve():
    """Index: 985.
    Returns: the number of pages that are neither crumpled nor blurred.
    """
    # L1
    total_pages = 42 # If he prints 42 pages
    crumple_frequency = 7 # crumples every seventh page
    crumpled_pages = total_pages / crumple_frequency

    # L2
    blur_frequency = 3 # blurs the ink on every third page
    blurred_pages = total_pages / blur_frequency

    # L4
    # L3 states "there are two, 21 and 42."
    double_counted_pages = 2 # there are two
    neither_crumpled_nor_blurred_pages = total_pages - crumpled_pages - blurred_pages + double_counted_pages

    # FA
    answer = neither_crumpled_nor_blurred_pages
    return answer