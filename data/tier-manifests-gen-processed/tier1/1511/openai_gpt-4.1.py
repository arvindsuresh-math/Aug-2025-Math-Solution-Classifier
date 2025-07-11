def solve():
    """Index: 1511.
    Returns: the total number of drawings in the first five pages.
    """
    # L1
    first_page_drawings = 5 # 5 drawings on the first page
    increase_per_page = 5 # increased by five after every page
    second_page_drawings = first_page_drawings + increase_per_page

    # L2
    total_2_pages = first_page_drawings + second_page_drawings

    # L3
    third_page_drawings = second_page_drawings + increase_per_page

    # L4
    total_3_pages = total_2_pages + third_page_drawings

    # L5
    fourth_page_drawings = third_page_drawings + increase_per_page

    # L6
    total_4_pages = total_3_pages + fourth_page_drawings

    # L7
    fifth_page_drawings = fourth_page_drawings + increase_per_page

    # L8
    total_5_pages = fifth_page_drawings + total_4_pages

    # FA
    answer = total_5_pages
    return answer