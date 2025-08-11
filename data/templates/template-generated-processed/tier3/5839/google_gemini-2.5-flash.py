def solve():
    """Index: 5839.
    Returns: the number of boxes of granola bars Katie's mother should buy.
    """
    # L1
    num_kids = 30 # 30 kids playing soccer
    bars_per_kid = 2 # 2 granola bars for each kid
    total_bars_needed = num_kids * bars_per_kid

    # L2
    bars_per_box = 12 # Each box of granola bars has 12 bars in it
    num_boxes = total_bars_needed / bars_per_box

    # FA
    answer = num_boxes
    return answer