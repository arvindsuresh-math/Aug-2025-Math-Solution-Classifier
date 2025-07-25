from fractions import Fraction

def solve():
    """Index: 669.
    Returns: the total number of items Bella will have.
    """
    # L1
    more_fraction = Fraction(2, 5) # 2/5 times more of each item
    current_marbles = 60 # currently has 60 marbles
    increased_marbles = more_fraction * current_marbles

    # L2
    total_marbles = current_marbles + increased_marbles

    # L3
    marbles_to_frisbees_ratio = 2 # two times as many marbles as frisbees
    current_frisbees = current_marbles / marbles_to_frisbees_ratio

    # L4
    increased_frisbees = more_fraction * current_frisbees

    # L5
    total_frisbees = current_frisbees + increased_frisbees

    # L6
    frisbees_more_than_cards = 20 # 20 more frisbees than deck cards
    current_deck_cards = current_frisbees - frisbees_more_than_cards

    # L7
    increased_deck_cards = more_fraction * current_deck_cards

    # L8
    total_deck_cards = current_deck_cards + increased_deck_cards

    # L9
    total_items = total_deck_cards + total_frisbees + total_marbles

    # FA
    answer = total_items
    return answer