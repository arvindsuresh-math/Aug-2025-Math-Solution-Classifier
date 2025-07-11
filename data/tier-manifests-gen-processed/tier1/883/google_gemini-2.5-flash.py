def solve():
    """Index: 883.
    Returns: the total number of bolts and nuts used for the project.
    """
    # L1
    num_boxes_bolts = 7 # 7 boxes of bolts
    bolts_per_box = 11 # each box containing 11 bolts
    total_bolts_purchased = num_boxes_bolts * bolts_per_box

    # L2
    bolts_left_over = 3 # 3 bolts ... left over
    bolts_used_for_project = total_bolts_purchased - bolts_left_over

    # L3
    num_boxes_nuts = 3 # 3 boxes of nuts
    nuts_per_box = 15 # each box containing 15 nuts
    total_nuts_purchased = num_boxes_nuts * nuts_per_box

    # L4
    nuts_left_over = 6 # 6 nuts left over
    nuts_used_for_project = total_nuts_purchased - nuts_left_over

    # L5
    total_used_for_project = bolts_used_for_project + nuts_used_for_project

    # FA
    answer = total_used_for_project
    return answer