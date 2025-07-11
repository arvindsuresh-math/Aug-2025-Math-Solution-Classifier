def solve():
    """Index: 652.
    Returns: the total number of boxes Tanika sold over the two days.
    """
    # L1
    saturday_boxes = 60 # sold 60 boxes on Saturday
    sunday_multiplier = 1.50 # sold 50% more than on Saturday
    sunday_boxes = saturday_boxes * sunday_multiplier

    # L2
    total_boxes = saturday_boxes + sunday_boxes

    # FA
    answer = total_boxes
    return answer