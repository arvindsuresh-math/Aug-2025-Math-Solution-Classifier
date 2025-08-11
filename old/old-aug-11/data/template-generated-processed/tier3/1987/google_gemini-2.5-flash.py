from fractions import Fraction

def solve():
    """Index: 1987.
    Returns: the number of green cards in the box.
    """
    # L1
    total_cards = 120 # 120 cards in a box
    red_fraction = Fraction(2, 5) # 2/5 of the cards are red
    red_cards = red_fraction * total_cards

    # L2
    non_red_cards = total_cards - red_cards

    # L3
    black_fraction = Fraction(5, 9) # 5/9 of the remainder are black
    black_cards = black_fraction * non_red_cards

    # L4
    green_cards = non_red_cards - black_cards

    # FA
    answer = green_cards
    return answer