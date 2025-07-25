from fractions import Fraction

def solve():
    """Index: 7264.
    Returns: the number of additional books Karson needs to buy.
    """
    # L1
    target_percentage = Fraction(90, 100) # 90% full
    library_capacity = 400 # capacity of Karson's home library is 400 books
    target_books = target_percentage * library_capacity

    # L2
    current_books = 120 # currently has 120 books
    books_to_buy = target_books - current_books

    # FA
    answer = books_to_buy
    return answer