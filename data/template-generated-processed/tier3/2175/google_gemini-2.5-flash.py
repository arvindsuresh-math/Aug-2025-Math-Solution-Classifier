from fractions import Fraction

def solve():
    """Index: 2175.
    Returns: the total number of books the three have together.
    """
    # L1
    beatrix_books = 30 # If Beatrix has 30 books
    alannah_more_than_beatrix = 20 # Alannah has 20 more books than Beatrix
    alannah_books = beatrix_books + alannah_more_than_beatrix

    # L2
    queen_fraction_more = Fraction(1, 5) # Queen has 1/5 times more books than Alannah
    queen_additional_books = queen_fraction_more * alannah_books

    # L3
    queen_total_books = alannah_books + queen_additional_books

    # L4
    total_books = queen_total_books + alannah_books + beatrix_books

    # FA
    answer = total_books
    return answer