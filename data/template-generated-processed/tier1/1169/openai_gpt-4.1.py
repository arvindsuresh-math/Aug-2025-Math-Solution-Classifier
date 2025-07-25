def solve():
    """Index: 1169.
    Returns: the number of cards Ben has left after giving some away.
    """
    # L1
    num_basketball_boxes = 4 # four boxes
    basketball_per_box = 10 # ten basketball cards in each box
    basketball_cards = num_basketball_boxes * basketball_per_box

    # L2
    num_baseball_boxes = 5 # five boxes
    baseball_per_box = 8 # eight baseball cards
    baseball_cards = num_baseball_boxes * baseball_per_box

    # L3
    total_cards = basketball_cards + baseball_cards

    # L4
    cards_given = 58 # gives 58 cards to his classmates
    cards_left = total_cards - cards_given

    # FA
    answer = cards_left
    return answer