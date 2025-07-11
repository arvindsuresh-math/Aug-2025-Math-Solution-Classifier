def solve():
    """Index: 1442.
    Returns: the number of weeks Jame can tear cards.
    """
    # L1
    cards_per_tear_session = 30 # He can tear 30 cards at a time
    tear_sessions_per_week = 3 # He tears cards 3 times a week
    cards_torn_per_week = cards_per_tear_session * tear_sessions_per_week

    # L2
    cards_per_deck = 55 # A new deck of cards has 55 cards
    num_decks = 18 # he buys 18 decks
    total_cards_bought = cards_per_deck * num_decks

    # L3
    weeks_can_go = total_cards_bought / cards_torn_per_week

    # FA
    answer = weeks_can_go
    return answer