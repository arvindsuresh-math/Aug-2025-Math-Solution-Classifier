def solve():
    """Index: 326.
    Returns: the average cost per book.
    """
    # L1
    initial_money = 236 # Fred had 236 dollars
    remaining_money = 14 # he had 14 dollars
    money_spent = initial_money - remaining_money

    # L2
    num_books = 6 # 6 books
    cost_per_book = money_spent / num_books

    # FA
    answer = cost_per_book
    return answer