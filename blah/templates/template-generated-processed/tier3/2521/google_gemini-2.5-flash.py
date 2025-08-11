def solve():
    """Index: 2521.
    Returns: the total number of cards they have in all.
    """
    # L1
    total_less_mara = 150 # Mara has 40 cards less than 150
    less_amount_mara = 40 # Mara has 40 cards less than 150
    mara_cards = total_less_mara - less_amount_mara

    # L2
    twice_factor = 2 # Mara has twice as many cards as Janet
    janet_cards = mara_cards / twice_factor

    # L3
    janet_more_than_brenda = 9 # Janet has 9 cards more than Brenda
    brenda_cards = janet_cards - janet_more_than_brenda

    # L4
    total_cards = mara_cards + janet_cards + brenda_cards

    # FA
    answer = total_cards
    return answer