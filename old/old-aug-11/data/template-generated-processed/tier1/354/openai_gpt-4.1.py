def solve():
    """Index: 354.
    Returns: the number of boxes Seth bought in the first place.
    """
    # L1
    boxes_left = 4 # Seth has 4 boxes of oranges left
    after_giving_away_half = boxes_left * 2

    # L2
    boxes_given_to_mom = 1 # gave a box to his mother
    total_boxes = after_giving_away_half + boxes_given_to_mom

    # FA
    answer = total_boxes
    return answer