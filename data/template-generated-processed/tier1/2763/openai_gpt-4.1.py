def solve():
    """Index: 2763.
    Returns: the total number of boxes Markeesha sold over the three days.
    """
    # L1
    friday_boxes = 30 # sold 30 boxes of crackers for her scout troop's fundraiser
    saturday_multiplier = 2 # sold twice as many as on Friday
    saturday_boxes = saturday_multiplier * friday_boxes

    # L2
    sunday_fewer = 15 # sold 15 fewer than Saturday
    sunday_boxes = saturday_boxes - sunday_fewer

    # L3
    total_boxes = friday_boxes + saturday_boxes + sunday_boxes

    # FA
    answer = total_boxes
    return answer