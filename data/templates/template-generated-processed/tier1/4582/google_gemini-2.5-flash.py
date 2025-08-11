def solve():
    """Index: 4582.
    Returns: the total number of cards Robie had in the beginning.
    """
    # L1
    boxes_given_away = 2 # gave away 2 boxes to his friends
    boxes_with_him = 5 # he has 5 boxes with him
    total_boxes_filled = boxes_given_away + boxes_with_him

    # L2
    cards_per_box = 10 # 10 cards in each box
    cards_in_boxes = total_boxes_filled * cards_per_box

    # L3
    cards_not_in_box = 5 # 5 cards were not placed in a box
    total_cards_beginning = cards_in_boxes + cards_not_in_box

    # FA
    answer = total_cards_beginning
    return answer