def solve():
    """Index: 1495.
    Returns: the total amount Sheryll paid for the books.
    """
    # L1
    original_book_cost = 5 # a book costs $5
    discount_per_book = 0.5 # discount of $0.5 each
    discounted_book_cost = original_book_cost - discount_per_book

    # L2
    num_books_bought = 10 # bought 10 books
    total_cost = discounted_book_cost * num_books_bought

    # FA
    answer = total_cost
    return answer