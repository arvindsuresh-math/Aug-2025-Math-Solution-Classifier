def solve():
    """Index: 1135.
    Returns: the amount of money Reggie has left after buying the books.
    """
    # L1
    num_books = 5 # bought 5 books
    cost_per_book = 2 # each of which cost $2
    total_cost = num_books * cost_per_book

    # L2
    initial_money = 48 # Reggie's father gave him $48
    money_left = initial_money - total_cost

    # FA
    answer = money_left
    return answer