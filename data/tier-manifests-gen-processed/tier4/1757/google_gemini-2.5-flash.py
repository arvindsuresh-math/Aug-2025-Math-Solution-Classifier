from fractions import Fraction

def solve():
    """Index: 1757.
    Returns: the number of more pages Arthur needs to read.
    """
    # L1
    book1_total_pages = 500 # 500-page book
    book1_percent_read = 0.8 # 80% of a 500-page book
    pages_read_book1 = book1_total_pages * book1_percent_read

    # L2
    book2_total_pages = 1000 # 1000 page book
    book2_fraction_read = Fraction(1, 5) # 1/5 of a 1000 page book
    pages_read_book2 = book2_total_pages * book2_fraction_read

    # L3
    total_pages_read = pages_read_book1 + pages_read_book2

    # L4
    reading_goal = 800 # 800 pages of reading over the summer
    pages_remaining = reading_goal - total_pages_read

    # FA
    answer = pages_remaining
    return answer