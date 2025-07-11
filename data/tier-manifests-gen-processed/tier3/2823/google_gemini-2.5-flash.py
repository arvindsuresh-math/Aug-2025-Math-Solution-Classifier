def solve():
    """Index: 2823.
    Returns: the number of boxes of apples left.
    """
    # L1
    boxes_saturday = 50 # 50 boxes of apples on Saturday
    boxes_sunday = 25 # 25 boxes on Sunday
    total_boxes = boxes_saturday + boxes_sunday

    # L2
    apples_per_box = 10 # 10 apples in each box
    total_apples_initial = total_boxes * apples_per_box

    # L3
    apples_sold = 720 # sold a total of 720 apples
    apples_left = total_apples_initial - apples_sold

    # L4
    boxes_left = apples_left / apples_per_box

    # FA
    answer = boxes_left
    return answer