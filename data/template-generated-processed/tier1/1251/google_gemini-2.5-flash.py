def solve():
    """Index: 1251.
    Returns: the total amount Josh spent.
    """
    # L1
    num_films = 9 # bought 9 films
    cost_per_film = 5 # Each film cost $5
    cost_films = num_films * cost_per_film

    # L2
    num_books = 4 # bought 4 books
    cost_per_book = 4 # each book cost $4
    cost_books = num_books * cost_per_book

    # L3
    num_cds = 6 # bought 6 CDs
    cost_per_cd = 3 # each CD cost $3
    cost_cds = num_cds * cost_per_cd

    # L4
    total_spent = cost_films + cost_books + cost_cds

    # FA
    answer = total_spent
    return answer