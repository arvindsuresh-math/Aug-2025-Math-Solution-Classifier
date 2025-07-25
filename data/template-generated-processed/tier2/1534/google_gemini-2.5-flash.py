def solve():
    """Index: 1534.
    Returns: the total number of books in the library.
    """
    # L1
    total_percent = 100 # WK
    children_percent = 35 # 35% of them are intended for children
    adult_percent = total_percent - children_percent

    # L2
    adult_books_count = 104 # 104 of them are for adults
    adult_percent_decimal = 0.65 # derived from 100% - 35% (from question)
    total_books = adult_books_count / adult_percent_decimal

    # FA
    answer = total_books
    return answer