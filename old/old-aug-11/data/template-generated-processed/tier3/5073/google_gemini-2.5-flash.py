def solve():
    """Index: 5073.
    Returns: the number of doughnuts given away at the end of the day.
    """
    # L1
    total_doughnuts = 300 # The bakery makes 300 doughnuts for the day
    doughnuts_per_box = 10 # Each box of doughnuts holds 10 doughnuts
    total_boxes_made = total_doughnuts / doughnuts_per_box

    # L2
    boxes_sold = 27 # sells 27 boxes of doughnuts
    boxes_leftover = total_boxes_made - boxes_sold

    # L3
    doughnuts_given_away = boxes_leftover * doughnuts_per_box

    # FA
    answer = doughnuts_given_away
    return answer