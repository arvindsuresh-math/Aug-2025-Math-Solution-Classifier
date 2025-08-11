def solve():
    """Index: 6684.
    Returns: the number of additional boxes needed to pack all muffins.
    """
    # L1
    available_boxes = 10 # only 10 available boxes
    muffins_per_box = 5 # 5 muffins in each box
    muffins_packed_in_available_boxes = available_boxes * muffins_per_box

    # L2
    total_muffins = 95 # The bakery made 95 muffins
    remaining_muffins = total_muffins - muffins_packed_in_available_boxes

    # L3
    boxes_still_needed = remaining_muffins / muffins_per_box

    # FA
    answer = boxes_still_needed
    return answer