def solve():
    """Index: 4208.
    Returns: the number of pages with text.
    """
    # L1
    total_pages = 98 # 98 pages long
    half_factor = 0.5 # Half of the pages
    image_pages = total_pages * half_factor

    # L2
    introduction_pages = 11 # 11 with an introduction
    remaining_pages = total_pages - image_pages - introduction_pages

    # L3
    text_pages = remaining_pages * half_factor

    # FA
    answer = text_pages
    return answer