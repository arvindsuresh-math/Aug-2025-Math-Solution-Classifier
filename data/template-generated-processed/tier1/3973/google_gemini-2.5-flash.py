def solve():
    """Index: 3973.
    Returns: the total number of Pokemon cards they have in all.
    """
    # L2
    jenny_cards = 6 # Jenny has 6 Pokemon cards
    orlando_more_than_jenny = 2 # Orlando has 2 more cards than Jenny
    orlando_cards = jenny_cards + orlando_more_than_jenny

    # L3
    richard_multiplier = 3 # Richard has three times as many cards as Orlando
    richard_cards = orlando_cards * richard_multiplier

    # L4
    total_cards = jenny_cards + orlando_cards + richard_cards

    # FA
    answer = total_cards
    return answer