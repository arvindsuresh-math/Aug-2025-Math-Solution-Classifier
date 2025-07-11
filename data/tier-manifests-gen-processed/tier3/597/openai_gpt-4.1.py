def solve():
    """Index: 597.
    Returns: the number of cards John now has after discarding some.
    """
    # L1
    cards_per_deck = 52 # Each deck of cards should hold 52 cards
    num_full_decks = 3 # 3 full decks of cards
    full_deck_cards = cards_per_deck * num_full_decks

    # L2
    half_deck_divisor = 2 # half-full deck
    half_deck_cards = cards_per_deck / half_deck_divisor

    # L3
    num_half_decks = 3 # 3 half-full decks of cards
    total_half_deck_cards = half_deck_cards * num_half_decks

    # L4
    total_cards = full_deck_cards + total_half_deck_cards

    # L5
    trashed_cards = 34 # throw 34 of the cards in the trash
    remaining_cards = total_cards - trashed_cards

    # FA
    answer = remaining_cards
    return answer