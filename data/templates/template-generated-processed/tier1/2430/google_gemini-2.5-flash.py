def solve():
    """Index: 2430.
    Returns: the total amount Whitney spent.
    """
    # L1
    books_whales = 9 # 9 books about whales
    books_fish = 7 # 7 books about fish
    total_books = books_whales + books_fish

    # L2
    cost_per_book = 11 # Each book cost $11
    cost_books = cost_per_book * total_books

    # L3
    cost_per_magazine = 1 # each magazine cost $1
    num_magazines = 3 # 3 magazines
    cost_magazines = cost_per_magazine * num_magazines

    # L4
    total_spent = cost_magazines + cost_books

    # FA
    answer = total_spent
    return answer