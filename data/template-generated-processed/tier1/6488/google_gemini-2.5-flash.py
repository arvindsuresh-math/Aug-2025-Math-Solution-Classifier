def solve():
    """Index: 6488.
    Returns: the total number of boxes packed by the charity organization.
    """
    # L1
    food_cost_per_box = 80 # Each box contains $80 worth of food
    supplies_cost_per_box = 165 # $165 worth of additional supplies
    cost_per_box = food_cost_per_box + supplies_cost_per_box

    # L2
    initial_boxes = 400 # distribute 400 boxes of food
    initial_spent_money = cost_per_box * initial_boxes

    # L3
    donor_multiplier = 4 # 4 times the amount of money
    donor_money = initial_spent_money * donor_multiplier

    # L4
    additional_boxes = donor_money / cost_per_box

    # L5
    total_boxes = additional_boxes + initial_boxes

    # FA
    answer = total_boxes
    return answer