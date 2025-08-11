def solve():
    """Index: 2193.
    Returns: the total amount of money Niles collects.
    """
    # L1
    hardcover_book_cost = 30 # $30 each for six hardcover books
    num_hardcover_books = 6 # six hardcover books
    hardcover_cost_per_member = hardcover_book_cost * num_hardcover_books

    # L2
    paperback_book_cost = 12 # $12 each for six paperback books
    num_paperback_books = 6 # six paperback books
    paperback_cost_per_member = paperback_book_cost * num_paperback_books

    # L3
    snacks_cost_per_member = 150 # $150/year towards snacks
    total_cost_per_member = hardcover_cost_per_member + paperback_cost_per_member + snacks_cost_per_member

    # L4
    num_members = 6 # Each of the six members
    total_money_collected = total_cost_per_member * num_members

    # FA
    answer = total_money_collected
    return answer