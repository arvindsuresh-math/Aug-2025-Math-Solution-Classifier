def solve():
    """Index: 7139.
    Returns: the number of times Rick must break groups into smaller groups.
    """
    # L1
    total_books = 400 # He has 400 books in total
    division_factor = 2 # divides them into two separate equally-sized categories
    books_after_1st_division = total_books / division_factor
    num_divisions = 1

    # L2
    books_after_2nd_division = books_after_1st_division / division_factor
    num_divisions += 1

    # L3
    books_after_3rd_division = books_after_2nd_division / division_factor
    num_divisions += 1

    # L4
    books_after_4th_division = books_after_3rd_division / division_factor
    num_divisions += 1

    # L5
    target_group_size = 25 # 24 other books
    number_of_divisions = num_divisions

    # FA
    answer = number_of_divisions
    return answer