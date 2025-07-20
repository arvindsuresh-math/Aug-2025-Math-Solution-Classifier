def solve():
    """Index: 3418.
    Returns: the total number of stamps in Stella's album.
    """
    # L1
    stamps_per_row_first_pages = 30 # 30 stamps in each of the first 10 pages
    rows_per_page_first_pages = 5 # 5 rows of 30 stamps
    stamps_per_page_first_pages = stamps_per_row_first_pages * rows_per_page_first_pages

    # L2
    num_first_pages = 10 # first 10 pages
    total_stamps_first_pages = stamps_per_page_first_pages * num_first_pages

    # L3
    total_pages = 50 # 50 pages in her collector's album
    remaining_pages = total_pages - num_first_pages

    # L4
    stamps_per_page_remaining = 50 # The rest of the pages each have 50 stamps
    total_stamps_remaining_pages = remaining_pages * stamps_per_page_remaining

    # L5
    total_stamps_album = total_stamps_remaining_pages + total_stamps_first_pages

    # FA
    answer = total_stamps_album
    return answer