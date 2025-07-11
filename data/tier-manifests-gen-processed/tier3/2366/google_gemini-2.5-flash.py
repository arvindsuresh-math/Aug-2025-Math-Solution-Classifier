def solve():
    """Index: 2366.
    Returns: the number of photos that can be placed on each of the remaining pages.
    """
    # L1
    photos_per_page_first_section = 3 # 3 photos each on the first 10 pages
    pages_first_section = 10 # first 10 pages
    photos_first_section = photos_per_page_first_section * pages_first_section

    # L2
    photos_per_page_second_section = 4 # 4 photos each on the next 10 pages
    pages_second_section = 10 # next 10 pages
    photos_second_section = photos_per_page_second_section * pages_second_section

    # L3
    pages_used = pages_first_section + pages_second_section

    # L4
    photos_placed = photos_first_section + photos_second_section

    # L5
    total_photos = 100 # 100 photos on vacation
    photos_remaining = total_photos - photos_placed

    # L6
    total_pages = 30 # photo album with 30 pages
    pages_remaining = total_pages - pages_used

    # L7
    photos_per_remaining_page = photos_remaining / pages_remaining

    # FA
    answer = photos_per_remaining_page
    return answer