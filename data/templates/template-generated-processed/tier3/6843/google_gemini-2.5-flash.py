def solve():
    """Index: 6843.
    Returns: the number of donuts left for Sophie.
    """
    # L1
    initial_boxes = 4 # bought 4 boxes of donuts
    boxes_given_to_mom = 1 # gave 1 box to her mom
    boxes_left_after_mom = initial_boxes - boxes_given_to_mom

    # L2
    donuts_per_box = 12 # 12 donuts in each box
    total_donuts_remaining_in_boxes = boxes_left_after_mom * donuts_per_box

    # L3
    half_divisor = 2 # half a dozen
    donuts_given_to_sister = donuts_per_box / half_divisor

    # L4
    donuts_left_for_sophie = total_donuts_remaining_in_boxes - donuts_given_to_sister

    # FA
    answer = donuts_left_for_sophie
    return answer