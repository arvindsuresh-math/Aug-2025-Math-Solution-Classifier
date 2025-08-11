from fractions import Fraction

def solve():
    """Index: 4606.
    Returns: the number of pages Nate needs to read to finish the book.
    """
    # L1
    total_pages = 400 # a 400-page book
    percentage_read = Fraction(20, 100) # 20% of the book
    pages_read = total_pages * percentage_read

    # L2
    pages_remaining = total_pages - pages_read

    # FA
    answer = pages_remaining
    return answer