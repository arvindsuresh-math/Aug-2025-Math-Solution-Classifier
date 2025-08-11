from fractions import Fraction

def solve():
    """Index: 1247.
    Returns: the number of more cards Ellis got than Orion.
    """
    # L1
    ellis_ratio_part = 11 # ratio of 11:9
    orion_ratio_part = 9 # ratio of 11:9
    total_ratio_parts = ellis_ratio_part + orion_ratio_part

    # L2
    total_cards = 500 # The number of cards in a card game was 500
    ellis_fraction_numerator = 11 # ratio of 11:9
    ellis_cards = Fraction(ellis_fraction_numerator, total_ratio_parts) * total_cards

    # L3
    orion_cards = total_cards - ellis_cards

    # L4
    difference_in_cards = ellis_cards - orion_cards

    # FA
    answer = difference_in_cards
    return answer