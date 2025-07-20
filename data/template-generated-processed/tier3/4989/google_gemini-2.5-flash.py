def solve():
    """Index: 4989.
    Returns: the total number of gift boxes Edmund can wrap in 3 days.
    """
    # L1
    wrapper_per_day = 90 # 90 inches of gift wrapper per day
    wrapper_per_box = 18 # 18 inches of gift wrapper per gift box
    boxes_per_day = wrapper_per_day / wrapper_per_box

    # L2
    num_days = 3 # every 3 days
    total_boxes = boxes_per_day * num_days

    # FA
    answer = total_boxes
    return answer