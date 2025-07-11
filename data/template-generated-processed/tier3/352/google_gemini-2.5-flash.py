def solve():
    """Index: 352.
    Returns: the number of pages Punger needs to buy.
    """
    # L1
    packs_of_cards = 60 # He buys 60 packs of baseball cards
    cards_per_pack = 7 # Each pack has 7 cards inside
    total_cards = packs_of_cards * cards_per_pack

    # L2
    cards_per_page = 10 # Each page can hold 10 cards
    pages_needed = total_cards / cards_per_page

    # FA
    answer = pages_needed
    return answer