def solve():
    """Index: 6455.
    Returns: the number of books Adam bought on his shopping trip.
    """
    # L1
    num_shelves = 4 # 4 shelves
    books_per_shelf = 20 # 20 books per shelf
    total_capacity = num_shelves * books_per_shelf

    # L2
    books_left_over = 2 # 2 books left over
    total_books_at_end = total_capacity + books_left_over

    # L3
    books_before_shopping = 56 # 56 books in his bookcase
    books_bought = total_books_at_end - books_before_shopping

    # FA
    answer = books_bought
    return answer