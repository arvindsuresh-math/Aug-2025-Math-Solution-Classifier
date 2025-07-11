def solve():
    """Index: 883.
    Returns: the total number of bolts and nuts used for the project.
    """
    # L1
    boxes_bolts = 7 # 7 boxes of bolts
    bolts_per_box = 11 # each box containing 11 bolts
    total_bolts = boxes_bolts * bolts_per_box

    # L2
    bolts_left_over = 3 # 3 bolts left over
    bolts_used = total_bolts - bolts_left_over

    # L3
    boxes_nuts = 3 # 3 boxes of nuts
    nuts_per_box = 15 # each box containing 15 nuts
    total_nuts = boxes_nuts * nuts_per_box

    # L4
    nuts_left_over = 6 # 6 nuts left over
    nuts_used = total_nuts - nuts_left_over

    # L5
    total_used = bolts_used + nuts_used

    # FA
    answer = total_used
    return answer