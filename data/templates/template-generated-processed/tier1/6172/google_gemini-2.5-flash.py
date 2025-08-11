def solve():
    """Index: 6172.
    Returns: the number of cards Jimmy has left.
    """
    # L1
    multiplier_mary = 2 # twice as many cards
    cards_given_to_bob = 3 # gives three cards to Bob
    mary_cards = multiplier_mary * cards_given_to_bob

    # L2
    jimmy_initial_cards = 18 # Jimmy has 18 cards
    jimmy_cards_left = jimmy_initial_cards - cards_given_to_bob - mary_cards

    # FA
    answer = jimmy_cards_left
    return answer