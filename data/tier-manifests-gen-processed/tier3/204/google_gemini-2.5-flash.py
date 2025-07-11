def solve():
    """Index: 204.
    Returns: the average number of pages per book.
    """
    # L1
    pages_per_inch = 80 # 80 pages is one inch thick
    stack_thickness_inches = 12 # 12 inches thick
    total_pages = pages_per_inch * stack_thickness_inches

    # L2
    num_books = 6 # 6 books
    pages_per_book = total_pages / num_books

    # FA
    answer = pages_per_book
    return answer