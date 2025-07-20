def solve():
    """Index: 7061.
    Returns: the total number of candles in all small boxes.
    """
    # L1
    num_big_boxes = 50 # 50 big boxes
    small_boxes_per_big_box = 4 # four small boxes each
    total_small_boxes = small_boxes_per_big_box * num_big_boxes

    # L2
    candles_per_small_box = 40 # 40 candles
    total_candles = candles_per_small_box * total_small_boxes

    # FA
    answer = total_candles
    return answer