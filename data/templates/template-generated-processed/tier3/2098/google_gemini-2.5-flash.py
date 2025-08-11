def solve():
    """Index: 2098.
    Returns: the total number of boxes Ms. Mosel fills each week.
    """
    # L1
    hens = 270 # 270 hens
    days_per_week = 7 # WK
    total_eggs_per_week = hens * days_per_week

    # L2
    eggs_per_box = 6 # boxes of 6
    total_boxes_per_week = total_eggs_per_week / eggs_per_box

    # FA
    answer = total_boxes_per_week
    return answer