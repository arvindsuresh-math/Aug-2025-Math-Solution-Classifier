def solve():
    """Index: 368.
    Returns: the cost of the stuffed animal.
    """
    # L1
    num_coloring_books = 2 # two coloring books
    coloring_book_price = 4 # $4 each
    coloring_books_total = num_coloring_books * coloring_book_price

    # L2
    num_peanut_packs = 4 # 4 packs of peanuts
    peanut_pack_price = 1.5 # $1.50 each pack
    peanuts_total = num_peanut_packs * peanut_pack_price

    # L3
    total_books_and_peanuts = coloring_books_total + peanuts_total

    # L4
    total_paid = 25 # gave the cashier $25
    stuffed_animal_cost = total_paid - total_books_and_peanuts

    # FA
    answer = stuffed_animal_cost
    return answer