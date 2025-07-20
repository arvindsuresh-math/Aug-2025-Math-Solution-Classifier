def solve():
    """Index: 4469.
    Returns: the total amount of the order.
    """
    # L1
    num_geography_books = 35 # 35 geography textbooks
    cost_geography_book = 10.5 # a geography book costs $10.50
    cost_geography_books = num_geography_books * cost_geography_book

    # L2
    num_english_books = 35 # 35 English textbooks
    cost_english_book = 7.5 # an English book costs $7.50
    cost_english_books = num_english_books * cost_english_book

    # L3
    total_order_amount = cost_geography_books + cost_english_books

    # FA
    answer = total_order_amount
    return answer