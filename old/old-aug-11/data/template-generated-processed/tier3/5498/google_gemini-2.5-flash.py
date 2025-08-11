def solve():
    """Index: 5498.
    Returns: the number of cards originally in the box.
    """
    # L1
    sasha_added_cards = 48 # Sasha added 48 cards
    fraction_taken_denominator = 6 # took out 1/6 of the cards
    cards_karen_took_out = sasha_added_cards / fraction_taken_denominator

    # L2
    current_total_cards = 83 # now 83 cards in the box
    net_cards_added_by_sasha = sasha_added_cards - cards_karen_took_out
    original_cards = current_total_cards - net_cards_added_by_sasha

    # FA
    answer = original_cards
    return answer