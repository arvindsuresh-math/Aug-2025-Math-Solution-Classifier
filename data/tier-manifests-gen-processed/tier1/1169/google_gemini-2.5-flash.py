def solve():
    """Index: 1169.
    Returns: the number of cards Ben has left.
    """
    # L1
    num_basketball_boxes = 4 # four boxes
    cards_per_basketball_box = 10 # ten basketball cards in each box
    total_basketball_cards = num_basketball_boxes * cards_per_basketball_box

    # L2
    num_baseball_boxes = 5 # five boxes
    cards_per_baseball_box = 8 # eight baseball cards
    total_baseball_cards = num_baseball_boxes * cards_per_baseball_box

    # L3
    total_cards_initial = total_basketball_cards + total_baseball_cards

    # L4
    cards_given_away = 58 # gives 58 cards to his classmates
    cards_left = total_cards_initial - cards_given_away

    # FA
    answer = cards_left
    return answer