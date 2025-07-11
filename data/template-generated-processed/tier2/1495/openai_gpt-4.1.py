def solve():
    """Index: 1495.
    Returns: the total amount Sheryll paid for the books.
    """
    # L1
    book_price = 5 # a book costs $5
    discount_per_book = 0.5 # discount of $0.5 each
    discounted_price = book_price - discount_per_book

    # L2
    num_books = 10 # bought 10 books
    total_paid = discounted_price * num_books

    # FA
    answer = total_paid
    return answer