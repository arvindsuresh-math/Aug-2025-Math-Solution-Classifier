def solve():
    """Index: 5837.
    Returns: the total cost to wrap all boxes.
    """
    # L1
    total_shirt_boxes = 20 # 20 shirt boxes to wrap
    shirt_boxes_per_roll = 5 # 5 shirt boxes
    rolls_for_shirts = total_shirt_boxes / shirt_boxes_per_roll

    # L2
    total_xl_boxes = 12 # 12 XL boxes to wrap
    xl_boxes_per_roll = 3 # 3 XL boxes
    rolls_for_xl = total_xl_boxes / xl_boxes_per_roll

    # L3
    total_rolls_needed = rolls_for_shirts + rolls_for_xl

    # L4
    cost_per_roll = 4.00 # $4.00 per roll
    total_cost = cost_per_roll * total_rolls_needed

    # FA
    answer = total_cost
    return answer