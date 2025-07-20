def solve():
    """Index: 4896.
    Returns: Grover's total profit from selling face masks.
    """
    # L1
    price_per_mask = 0.50 # $0.50 each
    masks_per_box = 20 # each box has 20 face masks
    earnings_per_box = price_per_mask * masks_per_box

    # L2
    num_boxes = 3 # 3 boxes of face masks
    total_earnings = earnings_per_box * num_boxes

    # L3
    cost_of_boxes = 15 # bought the 3 boxes for $15
    total_profit = total_earnings - cost_of_boxes

    # FA
    answer = total_profit
    return answer