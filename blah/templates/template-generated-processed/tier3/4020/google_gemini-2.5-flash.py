from fractions import Fraction

def solve():
    """Index: 4020.
    Returns: the number of history books.
    """
    # L1
    total_books = 10 # 10 books on the table
    reading_fraction = Fraction(2, 5) # Two-fifths of them are reading books
    reading_books = total_books * reading_fraction

    # L2
    math_fraction = Fraction(3, 10) # three-tenths of them are math books
    math_books = total_books * math_fraction

    # L3
    fewer_science_books = 1 # one fewer science book
    science_books = math_books - fewer_science_books

    # L4
    total_non_history_books = reading_books + math_books + science_books

    # L5
    history_books = total_books - total_non_history_books

    # FA
    answer = history_books
    return answer