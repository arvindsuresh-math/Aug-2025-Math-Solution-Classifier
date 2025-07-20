def solve():
    """Index: 3640.
    Returns: the amount of money Arthur has leftover.
    """
    # L1
    card_value_dollars = 0.05 # each card is worth 5 cents
    num_cards = 2000 # all 2,000 cards
    total_money_from_cards = card_value_dollars * num_cards

    # L2
    comic_book_cost = 6 # comic books cost $6 each
    num_comic_books_bought = total_money_from_cards // comic_book_cost

    # L3
    cost_of_comic_books = num_comic_books_bought * comic_book_cost

    # L4
    money_leftover = total_money_from_cards - cost_of_comic_books

    # FA
    answer = money_leftover
    return answer