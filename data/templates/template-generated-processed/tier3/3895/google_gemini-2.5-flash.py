from fractions import Fraction

def solve():
    """Index: 3895.
    Returns: the percentage of cards Joseph has left.
    """
    # L1
    initial_cards = 16 # Joseph had 16 baseball cards
    fraction_given_to_brother = Fraction(3, 8) # 3/8 of the cards
    cards_given_by_fraction = initial_cards * fraction_given_to_brother

    # L2
    additional_cards_given_to_brother = 2 # and 2 cards to his brother
    total_cards_given = cards_given_by_fraction + additional_cards_given_to_brother

    # L3
    cards_left = initial_cards - total_cards_given

    # L4
    percentage_multiplier = 100 # WK
    percentage_left = (cards_left / initial_cards) * percentage_multiplier

    # FA
    answer = percentage_left
    return answer