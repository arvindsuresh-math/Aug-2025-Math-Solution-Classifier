def solve():
    """Index: 652.
    Returns: the total number of boxes sold over the two days.
    """
    # L1
    boxes_sold_saturday = 60 # sold 60 boxes
    sunday_increase_factor = 1.50 # 50% more than on Saturday (100% + 50% = 150% or 1.50 times)
    boxes_sold_sunday = boxes_sold_saturday * sunday_increase_factor

    # L2
    total_boxes = boxes_sold_saturday + boxes_sold_sunday

    # FA
    answer = total_boxes
    return answer