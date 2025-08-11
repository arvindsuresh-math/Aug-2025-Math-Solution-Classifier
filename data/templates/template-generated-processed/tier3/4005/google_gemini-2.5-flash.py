def solve():
    """Index: 4005.
    Returns: the number of posters Shelby can buy.
    """
    # L1
    cost_book1 = 8 # bought one book for $8
    cost_book2 = 4 # and another for $4
    total_spent_on_books = cost_book1 + cost_book2

    # L2
    initial_money = 20 # Shelby had $20
    money_left = initial_money - total_spent_on_books

    # L3
    cost_per_poster = 4 # $4 posters
    num_posters = money_left / cost_per_poster

    # FA
    answer = num_posters
    return answer