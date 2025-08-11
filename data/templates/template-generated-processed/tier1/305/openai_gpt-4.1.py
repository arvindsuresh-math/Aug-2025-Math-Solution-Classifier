def solve():
    """Index: 305.
    Returns: the amount Tommy needs to save up to buy 8 new books.
    """
    # L1
    num_books = 8 # 8 new books
    cost_per_book = 5 # Each book costs $5
    total_cost = num_books * cost_per_book

    # L2
    tommy_has = 13 # Tommy already has $13
    amount_to_save = total_cost - tommy_has

    # FA
    answer = amount_to_save
    return answer