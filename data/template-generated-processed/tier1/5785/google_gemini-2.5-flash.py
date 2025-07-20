def solve():
    """Index: 5785.
    Returns: the number of picture books on the cart.
    """
    # L1
    fiction_books = 5 # five fiction books
    more_non_fiction_than_fiction = 4 # 4 more non-fiction books than fiction books
    non_fiction_books = fiction_books + more_non_fiction_than_fiction

    # L2
    multiplier_autobiographies = 2 # 2 times as many autobiographies as fiction books
    autobiographies = multiplier_autobiographies * fiction_books

    # L3
    total_known_books = fiction_books + non_fiction_books + autobiographies

    # L4
    total_books_on_cart = 35 # 35 books on the cart
    picture_books = total_books_on_cart - total_known_books

    # FA
    answer = picture_books
    return answer