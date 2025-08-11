def solve():
    """Index: 6998.
    Returns: the number of additional hours Jo will be reading the book.
    """
    # L1
    current_page = 90 # Now, she is at page 90
    page_an_hour_ago = 60 # An hour ago, she was at page 60
    pages_per_hour = current_page - page_an_hour_ago

    # L2
    total_pages = 210 # Her current book has 210 pages
    remaining_pages = total_pages - current_page

    # L3
    hours_needed = remaining_pages / pages_per_hour

    # FA
    answer = hours_needed
    return answer