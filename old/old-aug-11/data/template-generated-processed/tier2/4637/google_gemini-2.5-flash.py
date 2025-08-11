def solve():
    """Index: 4637.
    Returns: the total amount Travis spends on cereal.
    """
    # L1
    boxes_per_week = 2 # 2 boxes of cereal a week
    weeks_per_year = 52 # 52 weeks
    total_boxes = boxes_per_week * weeks_per_year

    # L2
    cost_per_box = 3.00 # each box costs $3.00
    total_spend = cost_per_box * total_boxes

    # FA
    answer = total_spend
    return answer