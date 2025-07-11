def solve():
    """Index: 2763.
    Returns: the total number of boxes sold over the three days.
    """
    # L1
    boxes_sold_friday = 30 # 30 boxes of crackers
    multiplier_saturday = 2 # twice as many as on Friday
    boxes_sold_saturday = multiplier_saturday * boxes_sold_friday

    # L2
    fewer_than_saturday = 15 # 15 fewer than Saturday
    boxes_sold_sunday = boxes_sold_saturday - fewer_than_saturday

    # L3
    total_boxes_sold = boxes_sold_friday + boxes_sold_saturday + boxes_sold_sunday

    # FA
    answer = total_boxes_sold
    return answer