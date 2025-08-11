def solve():
    """Index: 2912.
    Returns: the total number of books in the pyramid.
    """
    # L1
    top_level_books = 64 # top level has 64 books
    percent_per_level = 0.8 # Each level has 80% as many books as previous
    third_level_books = top_level_books / percent_per_level

    # L2
    second_level_books = third_level_books / percent_per_level

    # L3
    first_level_books = second_level_books / percent_per_level

    # L4
    total_books = top_level_books + third_level_books + second_level_books + first_level_books

    # FA
    answer = total_books
    return answer