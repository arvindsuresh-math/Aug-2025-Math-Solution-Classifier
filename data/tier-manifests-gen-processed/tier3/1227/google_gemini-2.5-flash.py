def solve():
    """Index: 1227.
    Returns: the number of additional boxes needed for loose crayons.
    """
    # L1
    total_crayons_francine = 85 # Francine has a total of 85 crayons
    loose_crayons_francine = 5 # 5 loose crayons
    crayons_in_boxes_francine = total_crayons_francine - loose_crayons_francine

    # L2
    num_full_boxes_francine = 5 # five full boxes of crayons
    crayons_per_box = crayons_in_boxes_francine / num_full_boxes_francine

    # L3
    loose_crayons_friend = 27 # her friend has 27 loose crayons
    total_loose_crayons = loose_crayons_francine + loose_crayons_friend

    # L4
    boxes_needed = total_loose_crayons / crayons_per_box

    # FA
    answer = boxes_needed
    return answer