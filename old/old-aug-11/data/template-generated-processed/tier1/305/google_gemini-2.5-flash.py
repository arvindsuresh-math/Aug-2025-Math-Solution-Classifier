def solve():
    """Index: 305.
    Returns: the amount of money Tommy needs to save up.
    """
    # L1
    num_books = 8 # 8 new books
    cost_per_book = 5 # Each book costs $5
    total_cost_books = num_books * cost_per_book

    # L2
    money_already_has = 13 # already has $13
    money_needed_to_save = total_cost_books - money_already_has

    # FA
    answer = money_needed_to_save
    return answer