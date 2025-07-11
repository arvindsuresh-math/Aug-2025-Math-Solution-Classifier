def solve():
    """Index: 2254.
    Returns: the number of cards each player has.
    """
    # L1
    initial_cards = 52 # 52 cards in it
    additional_cards = 2 # adds two additional cards
    total_cards = initial_cards + additional_cards

    # L2
    aubrey = 1 # herself
    other_players = 2 # two other players
    total_players = aubrey + other_players

    # L3
    cards_per_player = total_cards / total_players

    # FA
    answer = cards_per_player
    return answer