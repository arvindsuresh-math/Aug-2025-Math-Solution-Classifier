def solve():
    """Index: 560.
    Returns: the total money the student council will make.
    """
    # L1
    num_boxes = 48 # 48 boxes of erasers
    erasers_per_box = 24 # 24 erasers in each box
    total_erasers = num_boxes * erasers_per_box

    # L2
    price_per_eraser = 0.75 # $0.75 each
    total_money_made = total_erasers * price_per_eraser

    # FA
    answer = total_money_made
    return answer