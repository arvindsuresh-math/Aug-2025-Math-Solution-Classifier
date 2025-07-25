def solve():
    """Index: 7292.
    Returns: the total amount Marta spent on textbooks.
    """
    # L1
    num_sale_textbooks = 5 # five on sale
    cost_per_sale_textbook = 10 # $10 each
    total_sale_cost = num_sale_textbooks * cost_per_sale_textbook

    # L2
    num_bookstore_textbooks = 3 # three she bought directly from the bookstore
    cost_online_books = 40 # total of $40
    total_bookstore_cost = num_bookstore_textbooks * cost_online_books

    # L3
    total_spent = total_sale_cost + cost_online_books + total_bookstore_cost

    # FA
    answer = total_spent
    return answer