def solve():
    """Index: 4590.
    Returns: the total number of dozens of pomelos shipped by the farmer.
    """
    # L1
    total_pomelos_last_week = 240 # 240 pomelos in all
    boxes_last_week = 10 # 10 boxes of pomelos
    pomelos_per_box = total_pomelos_last_week / boxes_last_week

    # L2
    pomelos_per_dozen = 12 # WK
    dozens_per_box = pomelos_per_box / pomelos_per_dozen

    # L3
    boxes_this_week = 20 # 20 boxes
    total_boxes_shipped = boxes_last_week + boxes_this_week

    # L4
    total_dozens_shipped = total_boxes_shipped * dozens_per_box

    # FA
    answer = total_dozens_shipped
    return answer