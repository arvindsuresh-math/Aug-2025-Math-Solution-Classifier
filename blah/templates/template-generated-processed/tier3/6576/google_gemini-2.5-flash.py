def solve():
    """Index: 6576.
    Returns: the number of can lids from each box.
    """
    # L1
    total_lids_now = 53 # taking 53 can lids
    initial_lids = 14 # 14 can lids he already has
    lids_from_boxes = total_lids_now - initial_lids

    # L2
    num_boxes = 3 # 3 equal-sized boxes
    lids_per_box = lids_from_boxes / num_boxes

    # FA
    answer = lids_per_box
    return answer