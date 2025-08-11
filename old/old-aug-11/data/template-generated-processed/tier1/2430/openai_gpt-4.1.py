def solve():
    """Index: 2430.
    Returns: the total amount Whitney spent in all.
    """
    # L1
    whale_books = 9 # 9 books about whales
    fish_books = 7 # 7 books about fish
    total_books = whale_books + fish_books

    # L2
    book_cost = 11 # each book cost $11
    total_book_cost = book_cost * total_books

    # L3
    num_magazines = 3 # 3 magazines
    magazine_cost = 1 # each magazine cost $1
    total_magazine_cost = magazine_cost * num_magazines

    # L4
    total_spent = total_magazine_cost + total_book_cost

    # FA
    answer = total_spent
    return answer