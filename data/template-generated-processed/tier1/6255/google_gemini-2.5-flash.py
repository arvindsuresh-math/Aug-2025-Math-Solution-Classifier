def solve():
    """Index: 6255.
    Returns: the number of pages Rich has left to read to finish the book.
    """
    # L1
    pages_read = 125 # already read 125 pages of the book
    pages_skipped_maps = 16 # skipped the 16 pages of maps
    pages_completed = pages_read + pages_skipped_maps

    # L2
    total_pages = 372 # a 372-page book
    pages_left = total_pages - pages_completed

    # FA
    answer = pages_left
    return answer