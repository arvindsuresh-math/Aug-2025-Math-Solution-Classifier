def solve():
    """Index: 368.
    Returns: the cost of the stuffed animal.
    """
    # L1
    num_coloring_books = 2 # two coloring books
    cost_coloring_book = 4 # $4 each
    cost_coloring_books = num_coloring_books * cost_coloring_book

    # L2
    num_peanut_packs = 4 # 4 packs of peanuts
    cost_per_peanut_pack = 1.50 # $1.50 each pack
    cost_peanuts = num_peanut_packs * cost_per_peanut_pack

    # L3
    cost_books_and_peanuts = cost_coloring_books + cost_peanuts

    # L4
    cash_given = 25 # gave the cashier $25
    cost_stuffed_animal = cash_given - cost_books_and_peanuts

    # FA
    answer = cost_stuffed_animal
    return answer