def solve():
    """Index: 2720.
    Returns: the number of boxes of biscuits Kaylee still needs to sell.
    """
    # L1
    lemon_boxes = 12 # 12 boxes of lemon biscuits to her aunt
    chocolate_boxes = 5 # 5 boxes of chocolate biscuits to her mother
    oatmeal_boxes = 4 # 4 boxes of oatmeal biscuits to a neighbor
    boxes_sold = lemon_boxes + chocolate_boxes + oatmeal_boxes

    # L2
    total_needed = 33 # Kaylee needs to sell 33 boxes of biscuits
    boxes_remaining = total_needed - boxes_sold

    # FA
    answer = boxes_remaining
    return answer