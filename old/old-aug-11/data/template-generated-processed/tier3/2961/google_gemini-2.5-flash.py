from fractions import Fraction

def solve():
    """Index: 2961.
    Returns: the number of pages the middle book has.
    """
    # L1
    shortest_book_fraction = Fraction(1, 4) # one-fourth as many pages
    longest_book_pages = 396 # longest book has 396 pages
    shortest_book_pages = shortest_book_fraction * longest_book_pages

    # L2
    middle_book_multiplier = 3 # three times the number of pages
    middle_book_pages = middle_book_multiplier * shortest_book_pages

    # FA
    answer = middle_book_pages
    return answer