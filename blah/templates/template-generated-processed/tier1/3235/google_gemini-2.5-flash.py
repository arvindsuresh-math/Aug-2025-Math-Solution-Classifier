def solve():
    """Index: 3235.
    Returns: the number of pages remaining before Jerry can finish the book.
    """
    # L1
    total_pages = 93 # The book has 93 pages
    pages_read_saturday = 30 # On Saturday, he reads 30 pages
    remaining_after_saturday = total_pages - pages_read_saturday

    # L2
    pages_read_sunday = 20 # reads 20 pages of the book
    remaining_after_sunday = remaining_after_saturday - pages_read_sunday

    # FA
    answer = remaining_after_sunday
    return answer