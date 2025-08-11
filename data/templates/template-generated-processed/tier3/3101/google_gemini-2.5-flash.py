def solve():
    """Index: 3101.
    Returns: the total cost of syrup per week.
    """
    # L1
    gallons_per_week = 180 # 180 gallons of soda a week
    gallons_per_box = 30 # can make 30 gallons of soda
    num_boxes = gallons_per_week / gallons_per_box

    # L2
    cost_per_box = 40 # each box costs $40
    total_cost = num_boxes * cost_per_box

    # FA
    answer = total_cost
    return answer