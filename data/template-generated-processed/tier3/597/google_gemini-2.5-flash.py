def solve():
    """Index: 597.
    Returns: the total number of cards John has.
    """
    # L1
    cards_per_full_deck = 52 # Each deck of cards should hold 52 cards
    num_full_decks = 3 # 3 full decks of cards
    cards_from_full_decks = cards_per_full_deck * num_full_decks

    # L2
    half_divisor = 2 # half-full decks
    cards_per_half_deck = cards_per_full_deck / half_divisor

    # L3
    num_half_decks = 3 # 3 half-full decks of cards
    cards_from_half_decks = cards_per_half_deck * num_half_decks

    # L4
    total_cards_before_trash = cards_from_full_decks + cards_from_half_decks

    # L5
    trashed_cards = 34 # throw 34 of the cards in the trash
    final_cards = total_cards_before_trash - trashed_cards

    # FA
    answer = final_cards
    return answer