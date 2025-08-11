def solve():
    """Index: 2912.
    Returns: the total number of books in the pyramid.
    """
    # L1
    top_level_books = 64 # the top level has 64 books
    level_ratio = 0.8 # 80% as many books
    third_level_books = top_level_books / level_ratio

    # L2
    second_level_books = third_level_books / level_ratio

    # L3
    first_level_books = second_level_books / level_ratio

    # L4
    total_books = top_level_books + third_level_books + second_level_books + first_level_books

    # FA
    answer = total_books
    return answer