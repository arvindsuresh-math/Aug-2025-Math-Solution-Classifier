from fractions import Fraction

def solve():
    """Index: 931.
    Returns: the number of cards Malcom has left.
    """
    # L1
    brandon_cards = 20 # Brandon has a collection of 20 baseball cards
    more_cards = 8 # Malcom has 8 more cards than Brandon
    malcom_initial_cards = brandon_cards + more_cards

    # L2
    fraction_given_away_numerator = 1 # half of his cards
    fraction_given_away_denominator = 2 # half of his cards
    cards_given_away = Fraction(fraction_given_away_numerator, fraction_given_away_denominator) * malcom_initial_cards

    # L3
    malcom_remaining_cards = malcom_initial_cards - cards_given_away

    # FA
    answer = malcom_remaining_cards
    return answer