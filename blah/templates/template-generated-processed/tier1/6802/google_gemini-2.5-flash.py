def solve():
    """Index: 6802.
    Returns: the total number of dolls.
    """
    # L1
    big_box_dolls = 7 # Big boxes contain 7 dolls each
    num_big_boxes = 5 # 5 big boxes
    total_dolls_big_boxes = big_box_dolls * num_big_boxes

    # L2
    small_box_dolls = 4 # Small boxes contain 4 dolls each
    num_small_boxes = 9 # 9 small boxes
    total_dolls_small_boxes = small_box_dolls * num_small_boxes

    # L3
    total_dolls = total_dolls_big_boxes + total_dolls_small_boxes

    # FA
    answer = total_dolls
    return answer