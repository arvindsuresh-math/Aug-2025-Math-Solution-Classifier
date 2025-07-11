def solve():
    """Index: 326.
    Returns: the average cost per book Fred paid.
    """
    # L1
    initial_money = 236 # Fred had 236 dollars to spend
    money_left = 14 # he had 14 dollars
    money_spent = initial_money - money_left

    # L2
    num_books = 6 # 6 books
    cost_per_book = money_spent / num_books

    # FA
    answer = cost_per_book
    return answer