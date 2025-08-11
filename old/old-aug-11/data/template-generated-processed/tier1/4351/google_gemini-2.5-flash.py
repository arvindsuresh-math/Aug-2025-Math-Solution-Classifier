def solve():
    """Index: 4351.
    Returns: the amount of money Joe has left.
    """
    # L1
    num_notebooks = 7 # 7 notebooks
    cost_per_notebook = 4 # $4
    cost_notebooks = num_notebooks * cost_per_notebook

    # L2
    num_books = 2 # 2 books
    cost_per_book = 7 # $7
    cost_books = num_books * cost_per_book

    # L3
    total_spent = cost_notebooks + cost_books

    # L4
    initial_money = 56 # $56 to go to the store
    money_left = initial_money - total_spent

    # FA
    answer = money_left
    return answer