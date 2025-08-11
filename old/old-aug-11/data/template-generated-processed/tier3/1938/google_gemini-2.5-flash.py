def solve():
    """Index: 1938.
    Returns: the cost of each art book.
    """
    # L1
    num_math_books = 2 # She buys 2 math books
    cost_per_math_book = 3 # math and science books cost $3 each
    total_cost_math_books = num_math_books * cost_per_math_book

    # L2
    num_science_books = 6 # and 6 science books
    cost_per_science_book = 3 # math and science books cost $3 each
    total_cost_science_books = num_science_books * cost_per_science_book

    # L3
    total_cost_math_science = total_cost_math_books + total_cost_science_books

    # L4
    total_cost_all_books = 30 # for a total of $30
    total_cost_art_books = total_cost_all_books - total_cost_math_science

    # L5
    num_art_books = 3 # 3 art books
    cost_per_art_book = total_cost_art_books / num_art_books

    # FA
    answer = cost_per_art_book
    return answer