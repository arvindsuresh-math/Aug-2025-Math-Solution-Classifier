def solve():
    """Index: 354.
    Returns: the initial number of boxes of oranges Seth bought.
    """
    # L1
    boxes_left_after_giving_half = 4 # Seth has 4 boxes of oranges left
    multiplier_for_half = 2 # WK
    boxes_before_giving_half = boxes_left_after_giving_half * multiplier_for_half

    # L2
    box_given_to_mom = 1 # He gave a box to his mother
    initial_boxes_bought = boxes_before_giving_half + box_given_to_mom

    # FA
    answer = initial_boxes_bought
    return answer