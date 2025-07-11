def solve():
    """Index: 1534.
    Returns: the total number of books in the library.
    """
    # L1
    percent_total = 100 # WK (percentages sum to 100)
    percent_children = 35 # 35% of them are intended for children
    percent_adult = percent_total - percent_children

    # L2
    num_adult_books = 104 # 104 of them are for adults
    percent_adult_decimal = 0.65 # .65 (from 65%)
    total_books = num_adult_books / percent_adult_decimal

    # FA
    answer = total_books
    return answer