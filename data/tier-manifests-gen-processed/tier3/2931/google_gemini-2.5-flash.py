from fractions import Fraction

def solve():
    """Index: 2931.
    Returns: the total number of books in the class.
    """
    # L1
    books_per_table_fraction = Fraction(2, 5) # 2/5 times as many books
    num_tables = 500 # 500 tables
    books_on_each_table = books_per_table_fraction * num_tables

    # L2
    total_books = num_tables * books_on_each_table

    # FA
    answer = total_books
    return answer