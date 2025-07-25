def solve():
    """Index: 4763.
    Returns: the total amount Dave spent on the books.
    """
    # L1
    books_animals = 8 # 8 books about animals
    books_outer_space = 6 # 6 books about outer space
    books_trains = 3 # 3 books about trains
    total_books = books_animals + books_outer_space + books_trains

    # L2
    cost_per_book = 6 # Each book cost $6
    total_cost = total_books * cost_per_book

    # FA
    answer = total_cost
    return answer