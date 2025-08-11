from fractions import Fraction

def solve():
    """Index: 6262.
    Returns: the number of books Arlo bought.
    """
    # L1
    books_ratio_part = 7 # The ratio of books to pens ... is 7:3
    pens_ratio_part = 3 # The ratio of books to pens ... is 7:3
    total_ratio_parts = books_ratio_part + pens_ratio_part

    # L2
    books_ratio_fraction = Fraction(books_ratio_part, total_ratio_parts)
    total_stationery = 400 # bought a total of 400 stationery
    books_bought = books_ratio_fraction * total_stationery

    # FA
    answer = books_bought
    return answer