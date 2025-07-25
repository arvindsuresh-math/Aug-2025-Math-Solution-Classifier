def solve():
    """Index: 6153.
    Returns: the total amount Beatrice paid for the books.
    """
    # L1
    price_first_books = 20 # $20 for each of the first 5 books
    num_first_books = 5 # first 5 books
    cost_first_books = price_first_books * num_first_books

    # L2
    discount_amount = 2 # discount of $2
    discounted_price_per_book = price_first_books - discount_amount

    # L3
    total_books_bought = 20 # Beatrice bought 20 books
    num_discounted_books = total_books_bought - num_first_books

    # L4
    cost_discounted_books = num_discounted_books * discounted_price_per_book

    # L5
    total_cost = cost_first_books + cost_discounted_books

    # FA
    answer = total_cost
    return answer