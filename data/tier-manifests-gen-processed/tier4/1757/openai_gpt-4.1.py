from fractions import Fraction

def solve():
    """Index: 1757.
    Returns: the number of pages Arthur still needs to read to meet his goal.
    """
    # L1
    book1_total_pages = 500 # 500-page book
    book1_read_fraction = 0.8 # 80% of a 500-page book
    book1_pages_read = book1_total_pages * book1_read_fraction

    # L2
    book2_total_pages = 1000 # 1000 page book
    book2_read_fraction = Fraction(1, 5) # 1/5 of a 1000 page book
    book2_pages_read = book2_total_pages * book2_read_fraction

    # L3
    total_pages_read = book1_pages_read + book2_pages_read

    # L4
    goal_pages = 800 # needs to finish 800 pages
    pages_remaining = goal_pages - total_pages_read

    # FA
    answer = pages_remaining
    return answer