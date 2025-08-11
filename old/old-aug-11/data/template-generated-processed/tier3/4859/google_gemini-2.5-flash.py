def solve():
    """Index: 4859.
    Returns: the number of cards per layer in the house of cards.
    """
    # L1
    num_decks = 16 # 16 decks of cards
    cards_per_deck = 52 # 52 cards each
    total_cards = num_decks * cards_per_deck

    # L2
    num_layers = 32 # 32 layers tall
    cards_per_layer = total_cards / num_layers

    # FA
    answer = cards_per_layer
    return answer